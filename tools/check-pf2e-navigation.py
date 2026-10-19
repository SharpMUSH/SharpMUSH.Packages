#!/usr/bin/env python3
"""Offline source navigation checks; rules correctness still requires a player review.

Run from the package repository: python3 tools/check-pf2e-navigation.py
The real SharpMUSH PackageValidator separately validates the manifest and bodies.
"""
from collections import deque
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "pf2e-remaster" / "wiki"
LINK = re.compile(r"\[\[([^\]\r\n]+)\]\]")
START = "main:learn_pf2e"
JOURNEYS = {
    "check": ["main:character_sheet", "main:proficiency_ranks", "main:degrees_of_success"],
    "creation": ["main:character_creation_guide", "main:dwarf_fighter_example", "main:dwarf_wizard_example", "main:dwarf", "main:warrior", "main:fighter"],
    "equipment": ["main:equipment_basics", "main:longsword", "main:chain_mail", "main:steel_shield", "main:clan_dagger"],
    "encounter": ["main:encounter_mode", "main:multiple_attack_penalty", "main:first_encounter", "main:stride", "main:step", "main:size_and_reach", "main:trip", "main:strike"],
    "recovery": ["main:dying_and_recovery", "main:dying", "main:wounded", "main:unconscious", "main:hero_points"],
    "between encounters": ["main:treat_wounds", "main:medicine", "main:healers_toolkit"],
    "advancement": ["main:leveling_up", "main:dueling_parry", "main:hefty_hauler", "main:conceal_spell", "main:assurance"],
    "wizard": ["main:wizard_learning_guide", "main:spell_preparation", "main:basic_saving_throws", "main:wizard", "main:arcane_school", "main:school_of_battle_magic", "main:ignition", "main:electric_arc", "main:force_barrage", "main:force_bolt"],
    "reference": ["category:spells", "category:conditions", "category:dwarf_feats", "category:fighter_feats"],
}


# Instructional routes must be present on the decision page itself; reaching an
# option through an alphabetical directory does not repair a detached workflow.
DIRECT_EDGES = {
    "main:learn_pf2e": {"main:wizard_learning_guide", "main:dwarf_wizard_example", "main:first_encounter", "main:leveling_up"},
    "main:character_creation_guide": {"main:dwarf_fighter_example", "main:dwarf_wizard_example"},
    "main:dwarf_wizard_example": {
        "main:character_creation_guide", "main:wizard_learning_guide", "main:leveling_up",
        "main:dwarf", "main:rock_dwarf", "main:warrior", "main:wizard", "main:spellbook_blank",
    },
    "main:encounter_mode": {"main:stride", "main:step", "main:size_and_reach", "main:stand", "main:first_encounter"},
    "main:first_encounter": {"main:stride", "main:step", "main:size_and_reach", "main:encounter_mode", "main:dying_and_recovery"},
    "main:leveling_up": {"main:dwarf_wizard_example", "main:wizard_spellcasting", "main:conceal_spell", "main:assurance", "main:breathe_fire", "main:sure_strike"},
    "main:hero_points": {"main:dying", "main:wounded", "main:dying_and_recovery"},
    "main:dying": {"main:hero_points", "main:dying_and_recovery"},
    "main:wounded": {"main:hero_points"},
    "main:wizard_learning_guide": {"main:dwarf_wizard_example", "main:leveling_up", "main:spell_preparation", "main:basic_saving_throws", "main:arcane_school"},
    "main:wizard_spellcasting": {"main:spell_preparation", "main:cast_a_spell", "main:leveling_up", "main:dwarf_wizard_example"},
    "main:arcane_school": {
        "main:school_of_ars_grammatica", "main:school_of_battle_magic",
        "main:school_of_civic_wizardry", "main:school_of_mentalism",
        "main:school_of_protean_form", "main:school_of_the_boundary",
        "main:school_of_unified_magical_theory",
    },
}


def check():
    pages = {}
    errors = []
    for file in sorted(ROOT.glob("*/*.md")):
        if file.is_symlink() or file.stat().st_size > 1024 * 1024:
            errors.append(f"Unsupported symlink/oversized page: {file}")
            continue
        key = f"{file.parent.name}:{file.stem}"
        text = file.read_text(encoding="utf-8", errors="strict")
        pages[key] = text
        if key != "help:orc_license_notice" and "[[ORC License Notice|help:orc_license_notice]]" not in text:
            errors.append(f"Missing notice footer: {key}")
    graph = {}
    for key, text in pages.items():
        targets = []
        for match in LINK.finditer(text):
            target = match[1].split("|", 1)[-1]
            if target not in pages:
                errors.append(f"Missing or noncanonical wiki target in {key}: {target}")
            targets.append(target)
        graph[key] = targets
    for origin, required in DIRECT_EDGES.items():
        for target in sorted(required):
            if target not in graph.get(origin, []):
                errors.append(f"Missing direct instruction edge: {origin} -> {target}")
    if START not in pages:
        errors.append(f"Missing learning entry: {START}")
    reachable = {START} if START in pages else set()
    queue = deque(reachable)
    while queue:
        for target in graph[queue.popleft()]:
            if target in pages and target not in reachable:
                # Offline complete graph validation; this is never a request-time query.
                reachable.add(target)
                queue.append(target)
    # Only reachability is required; a hard-coded hop count would reward link shortcuts.
    for journey, required in JOURNEYS.items():
        for key in required:
            if key not in reachable:
                errors.append(f"{journey}: destination not reachable from learning entry: {key}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(pages)} pages, {sum(map(len, graph.values()))} wiki links, {len(JOURNEYS)} reachable journey groups; rule correctness not certified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
