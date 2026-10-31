"""Reserved Material screening. The ORC License does not license proper nouns (deities, places, organizations,
named characters, setting names) or Paizo's trademarks, so an item that holds one is reworded, has the sentence
cut, or is dropped.

The term list is SETTING plus every deity in the Foundry deities pack, less ALLOW and the deity names that are
ordinary words. REWORD and CUT are keyed by item name; DROP lists items whose rule is the proper noun itself.
Any other description that still names a term has that sentence cut, and the report lists it for review.
"""
import re

# Setting names: places, nations, peoples, organizations, planes and named things of the setting.
SETTING = [
	"Golarion", "Pathfinder Society", "Pathfinder", "Absalom", "Starstone", "Varisia", "Varisian", "Cheliax", "Chelaxian",
	"Andoran", "Andoren", "Taldor", "Taldan", "Taldane", "Qadira", "Qadiran", "Osirion", "Osirian", "Osiriani",
	"Katapesh", "Rahadoum", "Thuvia", "Geb", "Nex", "Alkenstar", "Numeria", "Ustalav", "Mendev", "Irrisen", "Brevoy",
	"River Kingdoms", "Galt", "Isger", "Molthune", "Nirmathas", "Lastwall", "Belkzen", "Mwangi", "Garund", "Garundi",
	"Avistan", "Tian Xia", "Tian", "Casmaron", "Vudra", "Vudrani", "Arcadia", "Sarkoris", "Worldwound", "Kyonin",
	"Jalmeray", "Minkai", "Hermea", "Druma", "Kalistrade", "Sargava", "Kellid", "Shoanti", "Ulfen", "Keleshite",
	"Kelesh", "Kelish", "Azlant", "Azlanti", "Thassilon", "Thassilonian", "Abendego", "Hellknight", "Hellknights",
	"Aspis", "Red Mantis", "Magaambya", "Grand Lodge", "Bellflower", "Firebrands", "Lion Blade", "Eagle Knight",
	"Gray Gardener", "Whispering Way", "Darklands", "Nidal", "Nidalese", "Razmiran", "Kaer Maga", "Magnimar",
	"Korvosa", "Riddleport", "Sandpoint", "Katheer", "Oprak", "Sothis", "Quantium", "Mana Wastes", "Jistka",
	"Earthfall", "Kortos", "Inner Sea", "Lost Omens", "Starfinder", "Eye of Dread", "Gravelands", "Impossible Lands",
	"Iobaria", "Mammoth Lords", "Realm of the Mammoth Lords", "Land of the Linnorm Kings", "Linnorm Kings",
	"Saga Lands", "Shackles", "Mordant Spire", "Holomog", "Senghor", "Nantambu", "Kibwe", "Ilizmagorti",
	"Dongun", "Goka", "Ravounel", "Thrune", "Aroden", "Arodenite", "Tar-Baphon", "Whispering Tyrant", "Lowls",
	"Sekamina", "Nar-Voth", "Orv", "Axis", "Boneyard", "Elysium", "Nirvana", "Maelstrom", "Dreamlands",
	"First World", "Outer Rifts", "Creation's Forge", "Netherworld", "Akashic Record", "Shadow Plane",
	"Plane of Shadow", "Great Beyond", "Universe", "Heaven", "Hell", "Abyss", "Abyssal", "Valeros", "Seelah",
	"Kyra", "Merisiel", "Ezren", "Harsk", "Amiri", "Lini", "Seoni", "Lem", "Kess", "Ostilli", "Korakai",
	"Droogami", "Golarian", "Iomedaean", "Sarenite", "Desnan", "Gozren", "Pharasman", "Torag", "Cayden",
	"Erastilian", "Nethysian", "Abadaran", "Calistrian", "Gorumite", "Zon-Kuthite", "Asmodean", "Norgorberite",
	"Rovagug", "Lamashtu", "Urgathoa", "Godclaw", "Sun Wukong", "Kami", "Akiton", "Castrovel", "Triaxus",
	"Aballon", "Apostae", "Eox", "Liavara", "Bretheda", "Verces", "Diaspora", "Damiar", "Ghol-Gan", "Tenebrous",
	"Paizo", "Kuthonite", "Kintargo", "Alabaster Academy", "Fleshforges", "Arcanamirium", "Skoan-Quah", "Kazavon",
	"College of Dimensional Studies", "School of Spells", "Barrowsiege", "Blackpeak", "Droskar's Crag", "Mhar Massif",
	"Pale Mountain", "Sakalayo", "Serithtial", "Mantis God", "Horseman of War", "Queen of the Night",
	"Horseman of the Apocalypse", "First Vault", "River of Souls", "Port Peril", "Farseer Tower", "Stone of the Seers",
	"Forge of Creation", "Skinsaw", "Jalmeri", "Manaket", "Academy of Applied Magic",
]
# Deity names that are ordinary English words or rules terms; matched only together with a deity cue.
COMMON_WORD_DEITIES = {"Set", "Vale", "Husk", "Nameless", "Monad", "Ng", "Nin", "Ra", "Myr", "Scal", "Cong", "Shei",
	"Rull", "Kols", "Inna", "Imot", "Varg", "Ulon", "Irez", "Ptah", "Bes", "Charon", "Norns", "Atropos",
	"Green Faith", "Green Man", "Hearth and Harvest", "Urban Prosperity", "Laws of Mortality", "The Devourer",
	"Faith in the Fallen", "Good Neighbors", "Sky Keepers", "Children of the Night", "Fortune's Fate",
	"The Last Breath", "The Endless Road", "God Calling", "Husk", "Smiad", "Trudd", "Elion", "Imbrex",
	"The Pale Horse", "The Divine Dare", "Radiant Prism", "Stone's Blood", "Weight of the World",
	"Keepers of the Hearth", "Touch of the Sun", "Essence Dancers", "Pillars of Knowledge", "Cosmic Caravan",
	"Shadow Cabinet", "Seafarers' Hope", "Eyes That Watch", "The Readied Strike", "The Offering Plate",
	"Demon Bringers", "Black Butterfly", "Mother Vulture", "Grandmother Spider", "The Lost Prince",
	"Atheists and Free Agents", "Wheels of Innovation", "Guardians of the Sacred Self", "Light of the Everlasting Flame",
	"The Freeing Flame", "Immaculate Growth", "The Green Mother", "Ydersius", "Lady Razor"}
# Words that read as setting names but are rules terms in these books; never flagged.
ALLOW = {"Heaven", "Hell", "Abyss", "Universe", "Kami", "Diaspora", "Tenebrous"}

# Rewordings applied to every description: planes with proper names become plain descriptions.
GLOBAL = [
	(r"Pathfinder (Player Core 2|Player Core|GM Core|Monster Core)", r"\1"),
	(r"Boneyard Lore", "Afterlife Lore"),
	(r"\bAxis Lore\b", "Plane of Law Lore"),
	(r"\bOuter Rifts Lore\b", "Abyss Lore"),
	(r"\bInto the Great Beyond\b", "Into the Planes"),
	(r"\bReligious Symbol of Pharasma\b", "Religious Symbol"),
	(r"\bthe Boneyard\b", "the realm of the dead"),
	(r"\bthe First World\b", "the realm of the fey"),
	(r"\bFirst World\b(?! (Adept|Magic))", "fey realm"),
	(r"\bthe Netherworld\b", "the plane of shadow"),
	(r"\bthe Outer Rifts\b", "the Abyss"),
	(r"\bthe Great Beyond\b", "the planes"),
	(r"\bthe wild realm of Elysium\b", "a wild celestial realm"),
	(r"\bfrom Nirvana or one of the other celestial realms\b", "from one of the celestial realms"),
	(r"\bfiends or the Maelstrom\b", "fiends or the plane of chaos"),
	(r" with energy from Creation's Forge", " with the energy of life"),
]
# Rewordings for one item: item name -> [(pattern, replacement)], applied to its description HTML.
REWORD = {
	"Anathema (Cleric)": [(r"anathema to (?:@UUID\[[^\]]*\]|Pharasma), the goddess of death", "anathema to a goddess of death")],
	"Deity (Cleric)": [(r"anathema to (?:@UUID\[[^\]]*\]|Pharasma), the goddess of death", "anathema to a goddess of death")],
	"Deity (Champion)": [(r"anathema to (?:@UUID\[[^\]]*\]|Pharasma), the goddess of death", "anathema to a goddess of death"),
		(r"outside the Pathfinder baseline", "outside the game's baseline")],
	"Blessed": [(r" \(such as Shelyn Lore\)", "")],
	"Raised by Belief": [(r" \(Abadar Lore, for example\)", "")],
	"Street Urchin": [(r" \(such as Absalom Lore or Magnimar Lore\)", "")],
	"Pulse of Civilization": [(r" \(such as Absalom Lore\)", "")],
	"Feybound": [(r"the First World or another realm of the fey", "a realm of the fey")],
	"Gnome": [(r"emigrated from the First World, realm of the fey", "emigrated from the realm of the fey"),
		(r"wandered to Golarion", "wandered into the mortal world")],
	"Ancestors": [(r", with the River of Souls itself,", ",")],
	"Pirate Dedication": [(r" \(such as Port Peril Lore\)", "")],
	"Lifewood Cage": [(r" from the Forge of Creation", "")],
	"Pursue a Lead": [(r""" or (&quot;|"|“)The Skinsaw Murders(&quot;|"|”)""", "")],
	"Wizard Spellcasting": [(r"Applications of Jalmeri Elemental Theory", "Applications of Elemental Theory")],
	"Human": [(r"As unpredictable and varied as any of Golarion's peoples", "As unpredictable and varied as any people"),
		(r"the realms around the Inner Sea", "the world")],
	"Composite Longbow": [(r"such as Erastil's favored weapon", "such as a deity's favored weapon")],
	"Duskwood Branch": [(r" in south-central Avistan", "")],
	"Duskwood Lumber": [(r" in south-central Avistan", "")],
	"Frozen Lava": [(r"on Golarion and across the planes", "across the world and the planes")],
	"Eye of Fortune": [(r"Adherents of Erastil, god of the hunt,", "Adherents of a god of the hunt")],
	"Forge Warden": [(r"The religious symbol of Torag, the forge god", "The religious symbol of a forge god"),
		(r"religious symbol of Torag", "religious symbol of a forge god")],
	"Martyr's Shield": [(r", like Iomedae or Vildeis,", "")],
	"Sash of Prowess": [(r", such as the open hand of Irori", "")],
	"Sash of Prowess (Greater)": [(r", such as the open hand of Irori", "")],
	"Sawtooth Saber": [(r"the Red Mantis assassins", "a secretive order of assassins")],
	"Trident of Lightning": [(r"Gozren motifs", "storm motifs")],
	"Wayfinder": [(r"<p><strong>Access</strong> member of the Pathfinder Society</p>", ""),
		(r"It serves as a badge of office for agents of the Pathfinder Society and as a status symbol among adventurers of any stripe\. ",
			"It serves as a status symbol among adventurers of any stripe. ")],
	"Deadly Simplicity": [(r" \(such as a fist, if you worship Irori\)", " (such as a fist)")],
	"Cavalier's Banner": [(r"a cavalier pledged to the church of Abadar would be held to the same standards as a cleric of that god",
		"a cavalier pledged to a church would be held to the same standards as a cleric of its god")],
	"Consecrate": [(r" \(such as undead for Pharasma or Sarenrae\)", " (such as undead for a deity of life)")],
	"Interplanar Teleport": [(r"such as the Plane of Fire, the Netherworld, or the Outer Rifts", "such as an elemental plane, the plane of shadow, or the Abyss")],
	"Clone": [(r"If Pharasma has decided", "If the judge of the dead has decided")],
	"Raise Dead": [(r"If Pharasma has decided", "If the judge of the dead has decided")],
	"Reincarnate": [(r"If Pharasma has decided", "If the judge of the dead has decided")],
	"Resurrect": [(r"If Pharasma has decided", "If the judge of the dead has decided")],
	"Stormtossed Tengu": [(r"a blessing from Hei Feng", "a divine blessing")],
}
# Items whose sentences naming a reserved term are flavor: each such sentence is cut.
CUT = {"Ancestors", "School of Mentalism", "School of Civic Wizardry", "Arcane School", "Battle", "Bones", "Cosmos", "Enigma", "Flames", "Life", "Lore",
	"Maestro", "Mystery", "Polymath", "School of Ars Grammatica", "School of Battle Magic", "School of Protean Form",
	"School of the Boundary", "Spinner of Threads", "Tempest", "Warrior", "Leadership", "Summon Celestial",
	"Summon Lesser Servitor", "Summon Monitor"}
# Pages dropped because the proper noun is the rule itself: item name -> reason.
DROP = {
	"Avatar": "the spell's battle forms are each a named deity's",
	"Serithtial": "a named intelligent artifact bound to named deities and a named dragon",
	"Shot of the First Vault": "an artifact tied to a named deity and a named plane",
	"Forgefather's Seal": "a rune made by and invoking a named deity",
	"Divine art piece created by Shelyn": "art object named for a deity",
	"Tankard owned by Cayden Cailean": "art object named for a deity",
	"Bronze brazier with Asmodean artwork": "art object named for a deity",
	"First World Adept": "feat named for a named plane",
	"First World Magic": "feat named for a named plane",
	"Boneyard's Call": "feat named for, and travelling to, a named plane",
	"Armageddon Orb": "a hazard forged from a named deity's blood and disabled through two named deities",
}
for _v in ("Barrowsiege", "Blackpeak", "Droskar's Crag", "Ka", "Mhar Massif", "Pale Mountain", "Sakalayo"):
	DROP[f"Frozen Lava of {_v}"] = "named for a volcano of the setting"
	DROP[f"Eternal Eruption of {_v}"] = "named for a volcano of the setting"


_PATTERN = None


def configure(deities):
	"""Build the term pattern from SETTING and the deity names of the Foundry deities pack."""
	global _PATTERN
	terms = sorted(set(SETTING + [n for n in deities if n not in COMMON_WORD_DEITIES]) - ALLOW, key=lambda s: (-len(s), s))
	alts = "|".join(re.escape(n) for n in terms)
	_PATTERN = re.compile(rf"(?<![\w-])({alts})(?![\w-])")


def hits(text):
	return sorted({m.group(1) for m in _PATTERN.finditer(text)})


def cut_sentences(html):
	"""Remove each sentence that names a reserved term."""
	for _ in range(200):
		m = _PATTERN.search(html)
		if not m:
			break
		before = html.rfind(". ", 0, m.start())
		start = max(before + 2 if before >= 0 else 0, html.rfind(">", 0, m.start()) + 1, html.rfind("? ", 0, m.start()) + 2)
		ends = [i for i in (html.find(". ", m.end()), html.find(".<", m.end()), html.find("? ", m.end()),
			html.find("?<", m.end())) if i >= 0]
		end = min(ends) + 1 if ends else len(html)
		if end < len(html) and html[end] == " ":
			end += 1
		html = html[:start] + html[end:]
	return html


DEITY_LINK = re.compile(r"@UUID\[Compendium\.pf2e\.deities\.Item\.([^\]]+)\](?:\{([^}]*)\})?")


def reword(name, html):
	"""The item's rewordings, the global ones, then a cut of any sentence still naming a term.

	Returns (html, how): how lists what was done, for the report."""
	how = []
	html = DEITY_LINK.sub(lambda m: m.group(2) or m.group(1), html)
	for pat, rep in REWORD.get(name, []):
		html, n = re.subn(pat, rep, html)
		if n:
			how.append("reworded")
	for pat, rep in GLOBAL:
		html, n = re.subn(pat, rep, html)
		if n:
			how.append("plane names replaced with plain descriptions")
	if _PATTERN.search(html):
		html = cut_sentences(html)
		how.append("sentences naming it cut" if name in CUT else "sentences naming it cut (not yet reviewed)")
	return html, sorted(set(how))


def text(s):
	"""The global rewordings, for a plain string such as a prerequisite or a Lore name."""
	for pat, rep in GLOBAL:
		s = re.sub(pat, rep, s)
	return s
