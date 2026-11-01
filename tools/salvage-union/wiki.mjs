// Builds salvage-union-wiki from the rules journals and compendiums of the Salvage Union (Unofficial) Foundry
// VTT system, at the same commit as build.mjs:
//
//   node wiki.mjs /tmp/su-foundry
//
// It rewrites salvage-union-wiki/package.yaml and everything under salvage-union-wiki/wiki/. A page of the
// journals becomes a page of the wiki, in a category for its chapter; every ability, mech system, module, pilot
// equipment, chassis and table gets a page of its own, and the journals' references to them become wiki links.
// The text is Salvage Union Core Book text, which the Salvage Union Open Game Licence 1.0b lets virtual tabletop
// content copy word for word; see salvage-union-wiki/NOTICE.md.

import { ClassicLevel } from 'classic-level';
import TurndownService from 'turndown';
import { gfm } from 'turndown-plugin-gfm';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const FOUNDRY_COMMIT = 'a1e47b514cda2af5ed423bce1c08523e8d235ae9'; // v1.3.0, as build.mjs

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.resolve(here, '../../salvage-union-wiki');
const foundry = process.argv[2];
if (!foundry) {
	console.error('usage: node wiki.mjs <foundry checkout>');
	process.exit(2);
}
const head = execFileSync('git', ['-C', foundry, 'rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
if (head !== FOUNDRY_COMMIT) {
	console.error(`${foundry} is at ${head}; this build reads ${FOUNDRY_COMMIT}.`);
	process.exit(1);
}

async function pack(name) {
	// Copied first: LevelDB takes a lock on the directory it opens.
	const copy = fs.mkdtempSync(path.join(os.tmpdir(), `su-${name}-`));
	fs.cpSync(path.join(foundry, 'packs', name), copy, { recursive: true });
	fs.rmSync(path.join(copy, 'LOCK'), { force: true });
	const db = new ClassicLevel(copy, { valueEncoding: 'json' });
	const rows = [];
	for await (const [key, value] of db.iterator()) rows.push({ key, ...value });
	await db.close();
	fs.rmSync(copy, { recursive: true, force: true });
	return rows;
}
const items = rows => rows.filter(row => row.key.startsWith('!items!') && row.type);

// ---- names ------------------------------------------------------------------------------------------------

const ASCII = [
	[/[‘’‚′]/g, "'"],
	[/[“”„″]/g, '"'],
	[/[–—−]/g, '-'],
	[/×/g, 'x'],
	[/…/g, '...'],
	[/ /g, ' '],
];
const ascii = text => ASCII.reduce((t, [from, to]) => t.replace(from, to), String(text ?? ''));
const slug = name =>
	ascii(name)
		.toLowerCase()
		.replace(/&[a-z]+;/g, '')
		.replace(/[^a-z0-9]+/g, '_')
		.replace(/^_+|_+$/g, '');

// Every page: its wiki name, title, categories and body. byId maps a Foundry document id to its page.
const pages = new Map();
const byId = new Map();
function page(base, title, categories, id) {
	let name = `main:su_${base}`;
	for (let n = 2; pages.has(name); n++) name = `main:su_${base}_${n}`;
	const entry = { name, title: ascii(title).trim(), categories, body: '' };
	pages.set(name, entry);
	if (id) byId.set(id, entry);
	return entry;
}

// ---- text -------------------------------------------------------------------------------------------------
// Foundry's enrichers become wiki links to the page of the document they name, or their label when the page
// does not exist (an ability's own gear). Links are swapped out before Turndown, which would escape them.

const turndown = new TurndownService({ headingStyle: 'atx', bulletListMarker: '-', emDelimiter: '*' });
turndown.use(gfm);
const chassisStats = new Map();

function markdown(html, self) {
	if (!html) return '';
	const tokens = [];
	const hold = text => `QQTOKEN${tokens.push(text) - 1}QQ`;
	const link = (ref, label) => {
		const id = /([A-Za-z0-9]{16})(?:#[^\]]*)?$/.exec(ref)?.[1];
		const target = byId.get(id);
		const text = ascii(label || target?.title || '').trim();
		if (!target || target === self) return text;
		return hold(`[[${text}|${target.name}]]`);
	};
	let text = String(html)
		.replace(/<li([^>]*)>\s*<p>([\s\S]*?)<\/p>\s*<\/li>/g, '<li$1>$2</li>')
		.replace(/@InlineChassis\[([^\]]*)\](?:\{[^}]*\})?/g, (_, ref) => hold(`\n\n${chassisStats.get(/([A-Za-z0-9]{16})$/.exec(ref)?.[1]) ?? ''}\n\n`))
		.replace(/@DisplayTable\w*\[([^\]]*)\](?:\{([^}]*)\})?/g, (_, ref, label) => {
			const table = byId.get(/([A-Za-z0-9]{16})$/.exec(ref)?.[1]);
			return table?.rows ? hold(`\n\n${table.rows}\n\n`) : link(ref, label);
		})
		.replace(/@\w+\[([^\]]*)\]\{([^}]*)\}/g, (_, ref, label) => link(ref, label))
		.replace(/@\w+\[([^\]]*)\]/g, (_, ref) => link(ref, ''))
		.replace(/\[\[\/r[^\]]*\]\]/g, '')
		.replace(/\s*\(?\bp\. ?\d+\)?(?=[\s.,;:)]|$)/g, '');
	text = ascii(turndown.turndown(text));
	return text
		.replace(/QQTOKEN(\d+)QQ/g, (_, n) => tokens[Number(n)])
		.replace(/[ \t]+$/gm, '')
		.replace(/^(\s*)(\d+)\.\s+/gm, '$1$2. ')
		.replace(/^(\s*)-\s+/gm, '$1- ')
		.replace(/\n{3,}/g, '\n\n')
		.trim();
}

const ACTIONS = { t: 'Turn Action', s: 'Short Action', l: 'Long Action', f: 'Free Action', r: 'Reaction', p: 'Passive', d: 'Downtime Action' };
const TECH = value => String(value ?? '').replace(/^T/i, '') || '1';
const capital = text => text.charAt(0).toUpperCase() + text.slice(1);
const line = parts => parts.filter(Boolean).join(' · ');
const traits = list => (list ?? []).filter(Boolean).map(ascii).join(', ');

// ---- documents --------------------------------------------------------------------------------------------
// The pages exist before any text is written, so a reference anywhere can link to any of them.

const tableRows = await pack('tables');
const tables = tableRows.filter(r => r.key.startsWith('!tables!')).sort((a, b) => a.name.localeCompare(b.name));
const results = tableRows.filter(r => r.key.startsWith('!tables.results!'));
for (const table of tables) {
	const title = ascii(table.name).replace(/ Table$/, '');
	page(`table_${slug(title)}`, `${title} Table`, ['su_tables'], table._id);
}

const abilityRows = await pack('abilities');
const folders = new Map(abilityRows.filter(r => r.key.startsWith('!folders!')).map(r => [r._id, r]));
const abilities = items(abilityRows)
	.filter(item => item.system?.level)
	.sort((a, b) => a.sort - b.sort);
const treeOf = item => {
	const folder = folders.get(item.folder);
	const owner = folders.get(folder.folder);
	const hybrid = folders.get(owner.folder).name.startsWith('Hybrid');
	if (folder.name === 'Legendary') return `Legendary ${owner.name}`;
	if (folder.name === 'Advanced') return hybrid ? `${owner.name} (Hybrid Class)` : `Advanced ${owner.name}`;
	return folder.name;
};
for (const item of abilities) page(slug(item.name), item.name, ['su_abilities'], item._id);

const kinds = [
	['systems', 'system', 'su_systems', 'System'],
	['modules', 'module', 'su_modules', 'Module'],
	['equipment', 'equipment', 'su_equipment', 'Pilot Equipment'],
];
const parts = {};
for (const [packName, , category] of kinds) {
	parts[packName] = items(await pack(packName))
		.filter(item => packName !== 'equipment' || item.system.inventorySlot === true)
		.sort((a, b) => TECH(a.system.techLevel) - TECH(b.system.techLevel) || a.name.localeCompare(b.name));
	for (const item of parts[packName]) page(slug(item.name), item.name, [category], item._id);
}

const chassis = items(await pack('chassis'));
for (const item of chassis) {
	const s = item.system;
	chassisStats.set(
		item._id,
		[
			'| Tech | SP | EP | Heat Capacity | System Slots | Module Slots | Cargo | Salvage Value |',
			'|---|---|---|---|---|---|---|---|',
			`| ${TECH(s.techLevel)} | ${s.sp} | ${s.ep} | ${s.heat} | ${s.systemSlots} | ${s.moduleSlots} | ${s.cargo} | ${s.salvageValue} |`,
			'',
			markdown(s.description),
		].join('\n'),
	);
}

// The chapters, in the order of the Core Book. A chassis blueprint page is the chassis' page; the Tech pages
// between them only name the Tech Level, and the chassis category lists them by it instead.
const CHAPTERS = ['Core Rules', 'Pilot Bay', 'Mech Workshop', 'Mech Chassis Blueprints', 'Union Crawler', 'Salvaging', 'Denizens of the Wasteland', 'Keywords and Traits'];
const journalRows = await pack('journals');
const journals = journalRows.filter(r => r.key.startsWith('!journal!'));
const journalPages = new Map(journalRows.filter(r => r.key.startsWith('!journal.pages!')).map(r => [r._id, r]));
const chapters = [];
for (const title of CHAPTERS) {
	const journal = journals.find(j => j.name === title);
	if (!journal) throw new Error(`no journal ${title}`);
	const category = `su_${slug(title)}`;
	const entries = [];
	for (const id of journal.pages) {
		const jp = journalPages.get(id);
		if (title === 'Mech Chassis Blueprints' && /^Tech \d$/.test(jp.name)) continue;
		const isChassis = title === 'Mech Chassis Blueprints';
		const entry = page(slug(jp.name), jp.name, isChassis ? ['su_chassis'] : [category], id);
		entries.push({ entry, jp });
		if (isChassis) {
			const item = chassis.find(c => c.name === jp.name);
			if (!item) throw new Error(`no chassis ${jp.name}`);
			byId.set(item._id, entry);
			entry.tech = TECH(item.system.techLevel);
		}
	}
	byId.set(journal._id, entries[0].entry);
	chapters.push({ title, category, journal, entries });
}

// ---- bodies -----------------------------------------------------------------------------------------------

const tableOf = ref => byId.get(/([A-Za-z0-9]{16})$/.exec(ref || '')?.[1]);
const seeTable = ref => (tableOf(ref) ? `\n\nRolls on the [[${tableOf(ref).title}|${tableOf(ref).name}]].` : '');

for (const table of tables) {
	const entry = byId.get(table._id);
	const rows = results.filter(r => r.key.split('!')[2].split('.')[0] === table._id).sort((a, b) => a.range[0] - b.range[0]);
	const cell = text => markdown(text).replace(/\n+/g, ' ').replace(/\|/g, '\\|');
	entry.rows = [
		`**${entry.title}**`,
		'',
		'| Roll | Result |',
		'|---|---|',
		...rows.map(r => {
			const high = Math.min(r.range[1], 20);
			return `| ${r.range[0] === high ? high : `${r.range[0]}-${high}`} | ${cell(r.text) || cell(r.name)} |`;
		}),
	].join('\n');
	entry.body = `${markdown(table.description, entry)}\n\n${entry.rows}`;
}

for (const item of abilities) {
	const s = item.system;
	const entry = byId.get(item._id);
	entry.body = [
		`**${ascii(treeOf(item))} Tree**`,
		line([s.ap !== '' && s.ap != null ? `${String(s.ap).toUpperCase()} AP` : '', ACTIONS[s.action], s.range ? `${capital(ascii(s.range))} Range` : '', traits(s.traits)]),
		'',
		markdown(s.description, entry) + seeTable(s.table_id),
	]
		.filter((l, i) => l || i === 2)
		.join('\n');
}

for (const [packName, , , label] of kinds) {
	for (const item of parts[packName]) {
		const s = item.system;
		const entry = byId.get(item._id);
		entry.tech = TECH(s.techLevel);
		entry.body = [
			`**Tech ${entry.tech} ${label}**`,
			line([
				s.slots ? `${s.slots} Slots` : '',
				s.salvageValue ? `Salvage Value ${s.salvageValue}` : '',
				s.ep !== '' && s.ep != null ? `${String(s.ep).toUpperCase()} EP` : '',
				s.ap !== '' && s.ap != null && packName === 'equipment' ? `${String(s.ap).toUpperCase()} AP` : '',
				s.range ? `${capital(ascii(s.range))} Range` : '',
				s.damage ? `Damage ${ascii(s.damage)}` : '',
				s.uses?.max ? `Uses ${s.uses.max}` : '',
				ACTIONS[s.action],
			]),
			traits(s.traits) ? `Traits: ${traits(s.traits)}` : '',
			'',
			markdown(s.description, entry) + seeTable(s.table_id),
		]
			.filter((l, i, all) => l || i === all.length - 2)
			.join('\n');
	}
}

for (const chapter of chapters) for (const { entry, jp } of chapter.entries) entry.body = markdown(jp.text?.content, entry);

// ---- categories and the landing page ----------------------------------------------------------------------

const link = entry => `[[${entry.title}|${entry.name}]]`;
const byTech = list => {
	const out = [];
	for (let tech = 1; tech <= 6; tech++) {
		const here = list.filter(e => e.tech === String(tech));
		if (here.length) out.push(`## Tech ${tech}`, '', ...here.map(e => `- ${link(e)}`), '');
	}
	return out.join('\n').trim();
};
const categoryPages = [];
const category = (name, title, body) => categoryPages.push({ name: `category:${name}`, title, body });

for (const chapter of chapters.filter(c => c.title !== 'Mech Chassis Blueprints')) {
	category(chapter.category, chapter.title, chapter.entries.map(({ entry }) => `- ${link(entry)}`).join('\n'));
}
const pick = list => list.map(item => byId.get(item._id));
category('su_chassis', 'Mech Chassis', byTech(chapters.find(c => c.title === 'Mech Chassis Blueprints').entries.map(e => e.entry)));
category('su_systems', 'Mech Systems', byTech(pick(parts.systems)));
category('su_modules', 'Mech Modules', byTech(pick(parts.modules)));
category('su_equipment', 'Pilot Equipment', byTech(pick(parts.equipment)));
const trees = new Map();
for (const item of abilities) {
	const tree = ascii(treeOf(item));
	if (!trees.has(tree)) trees.set(tree, []);
	trees.get(tree).push(byId.get(item._id));
}
category('su_abilities', 'Abilities', [...trees].map(([tree, list]) => `## ${tree} Tree\n\n${list.map(e => `- ${link(e)}`).join('\n')}`).join('\n\n'));
category('su_tables', 'Tables', tables.map(t => `- ${link(byId.get(t._id))}`).join('\n'));

const named = title => [...pages.values()].find(p => p.title === title);
const FOOTER = "*Salvage Union rules text from the Salvage Union (Unofficial) Foundry VTT system. Salvage Union is copyrighted by Leyline Press. See [[Salvage Union License Notice|help:salvage_union_license_notice]].*";
const landing = `Salvage Union is a game of salvagers in huge mechs, crossing a ruined world on a moving city called the Union Crawler. Everything in it is resolved by one twenty-sided die, read on the Core Mechanic table.

## How to play

- [[Core Rules|category:su_core_rules]]: ${chapters[0].entries.map(e => e.entry.title).join(', ')}.
- [[Pilot Bay|category:su_pilot_bay]]: making a pilot, the classes and their ability trees, and pilot equipment.
- [[Mech Workshop|category:su_mech_workshop]]: building a mech, its stats, systems and modules.
- [[Mech Chassis|category:su_chassis]]: every chassis blueprint, by Tech Level.
- [[Union Crawler|category:su_union_crawler]]: the crawler, its bays, upkeep and the downtime procedure.
- [[Salvaging|category:su_salvaging]]: salvage, scrap and cargo.
- [[Denizens of the Wasteland|category:su_denizens_of_the_wasteland]]: NPCs, morale and reaction rolls, for the Mediator.
- [[Keywords and Traits|category:su_keywords_and_traits]].

## Reference

- [[Abilities|category:su_abilities]], [[Mech Systems|category:su_systems]], [[Mech Modules|category:su_modules]], [[Pilot Equipment|category:su_equipment]] and [[Tables|category:su_tables]].

## Playing on this game

[[Salvage Union on this game|main:su_on_this_game]] lists the commands: \`+sheet\`, \`+mech\`, \`+check\`, \`+crawler\` and \`+encounter\`.

::: wiki-next-step
### Begin

Read the ${link(named('Core Mechanic'))}, then make your pilot with ${link(named('Pilot Creation'))} and your mech with ${link(named('Mech Creation'))}.
:::

---

${FOOTER}`;

const onThisGame = `This game keeps your Salvage Union pilot, mech and Union Crawler for you. \`+help sheet\`, \`+help mech\`, \`+help check\`, \`+help crawler\` and \`+help encounter\` explain each command in full.

## Your pilot

- \`+sheet/chargen\` lists the steps of making a pilot and their mech, and which are done.
- \`+sheet/class <class>\`, \`+sheet/learn <ability>\` and \`+sheet/take <equipment>\` build your pilot; \`+sheet/callsign\`, \`/background\`, \`/motto\`, \`/keepsake\` and \`/appearance\` write the details.
- \`+sheet\` shows your sheet; \`+sheet/hp\` and \`+sheet/ap\` keep count in play, and \`+sheet/use <equipment>\` spends a use.
- \`+sheet/learn\` after approval spends the Training Points staff award; \`+sheet/ledger\` lists every entry that built your sheet, and staff can take one back.
- After a week of downtime, staff run \`+sheet/downtime\`: HP, AP, re-rolls and uses come back, and you may take one piece of equipment from the Armoury.

## Your mech

- \`+mech/chassis <chassis>\` and \`+mech/install <system or module>\` build it; a new pilot builds from Tech 1 parts within 20 scrap, chassis included.
- Once approved, \`+mech/craft <part>\` gets a new chassis, system or module from the Union Crawler for its Salvage Value in scrap.
- \`+mech\` shows it; \`+mech/sp\`, \`/ep\` and \`/heat\` keep count, \`+mech/use\` spends a use, and \`+mech/vent\` cools it.

## Rolling

- \`+check [<ability, system or module>]\` rolls the die on the Core Mechanic table, spending AP or EP.
- \`+check/push\` re-rolls for 2 Heat, then makes the Heat Check; \`+check/reroll background\` and \`/reroll keepsake\` use a re-roll, and \`+check/motto <pilot>\` lets another pilot re-roll.
- \`+check/table <table>\` rolls on a table.

## The Union Crawler

\`+crawler\` shows the crawler the pilots share: its type, Tech Level, bays, scrap in the hold and upkeep. \`+crawler/unload\` moves your mech's scrap into the hold, \`+crawler/trade\` trades it at the Trading Bay, and \`+crawler/ledger\` lists every change to it.

## Encounters

A fight, a salvage run or another scene can be an encounter with its own copy of each member's sheet. \`+encounter/start [<title>]\` starts one and makes you its GM; \`+encounter/join\` takes a copy of your sheet into it. While you are in the room where it runs, your HP, AP, mech, re-rolls and uses are that copy, so an encounter that runs for days changes neither your sheet nor another scene. When it ends, only what the GM kept with \`+encounter/keep\` is on your sheet.

## Duties

Automated Duties roll on your own sheet, never on an encounter's copy.

---

${FOOTER}`;

const license = `The Salvage Union pages on this wiki and the Salvage Union sheet use material from the Salvage Union Core Book, through the Salvage Union (Unofficial) Foundry VTT system.

Salvage Union is copyrighted by Leyline Press. Salvage Union and the “Powered by Salvage” logo are used with permission of Leyline Press, under the Salvage Union Open Game Licence 1.0b .

This is not an official Leyline Press product, and it is not endorsed by Leyline Press. It holds no Leyline Press or Salvage Union logos, branding or art.`;

// ---- write ------------------------------------------------------------------------------------------------

const file = name => {
	const [space, rest] = name.split(':');
	return `wiki/${space}/${rest}.md`;
};
fs.rmSync(path.join(out, 'wiki'), { recursive: true, force: true });
const write = (name, body) => {
	const target = path.join(out, file(name));
	fs.mkdirSync(path.dirname(target), { recursive: true });
	fs.writeFileSync(target, `${body.trim()}\n`);
};

const yaml = [
	'format: "1.16"',
	'package: salvage-union-wiki',
	'title: Salvage Union rules',
	'version: 1.0.1',
	'wiki_landing_page: category:salvage_union_start_here',
	'wiki_collection_name: Salvage Union',
	'authors: [SharpMUSH]',
	'description: >-',
	'  The Salvage Union rules as wiki pages: the core rules, the Pilot Bay, the Mech Workshop, every',
	'  chassis blueprint, the Union Crawler, salvaging, the denizens of the wasteland, keywords and',
	'  traits, and a page for every ability, mech system, module, piece of pilot equipment and table.',
	'  Unofficial; used under the Salvage Union Open Game Licence 1.0b.',
	'license: LicenseRef-Salvage-Union-OGL-1.0b',
	'homepage: https://github.com/SharpMUSH/SharpMUSH.Packages/tree/main/salvage-union-wiki',
	'keywords: [salvage-union, rules, wiki, mechs]',
	'category: Characters',
	'locale: en',
	'',
	`# Generated by tools/salvage-union/wiki.mjs from the Salvage Union (Unofficial) Foundry VTT system`,
	`# ${FOUNDRY_COMMIT.slice(0, 7)} (v1.3.0). Do not edit by hand: change wiki.mjs and run it again.`,
	'# A content pack: wiki pages only, no objects or softcode. Softcode never reads these pages. The sheet that',
	'# plays these rules is sheet-salvage-union; this package does not need it, and it does not need this one.',
	'wiki:',
];
const entry = (name, title, categories, extra = []) => {
	yaml.push(`  - page: ${name}`, `    title: ${JSON.stringify(title)}`);
	if (categories?.length) yaml.push(`    categories: [${categories.join(', ')}]`);
	yaml.push(...extra, `    file: ${file(name)}`, '');
};

entry('category:salvage_union_start_here', 'Start here - Salvage Union', [], ['    pin: true']);
write('category:salvage_union_start_here', landing);
entry('help:salvage_union_license_notice', 'Salvage Union License Notice', [], ['    requires:', '      edit: [wiki.admin]', '      delete: [wiki.admin]']);
write('help:salvage_union_license_notice', license);
entry('main:su_on_this_game', 'Salvage Union on this game', ['salvage_union_start_here']);
write('main:su_on_this_game', onThisGame);
for (const c of categoryPages) {
	entry(c.name, c.title, ['salvage_union_start_here']);
	write(c.name, `${c.body}\n\n---\n\n${FOOTER}`);
}
for (const p of pages.values()) {
	entry(p.name, p.title, p.categories);
	write(p.name, `${p.body}\n\n---\n\n${FOOTER}`);
}
fs.writeFileSync(path.join(out, 'package.yaml'), yaml.join('\n').trimEnd() + '\n');
console.log(`${pages.size + categoryPages.length + 3} pages: ${chapters.reduce((n, c) => n + c.entries.length, 0)} from the journals, ${abilities.length} abilities, ${parts.systems.length} systems, ${parts.modules.length} modules, ${parts.equipment.length} equipment, ${tables.length} tables, ${categoryPages.length} categories.`);
