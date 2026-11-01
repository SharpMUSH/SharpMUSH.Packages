This game keeps your JRPG character sheet for you. `+help sheet`, `+help check` and `+help encounter` explain each command in full.

## Your sheet

- `+sheet` shows your sheet; `+sheet/traits` lists the attributes, classes, difficulties, status effects and emotions.
- `+sheet/set <attribute>=<die>`, `+sheet/class <class>=<levels>` and `+sheet/skill <class>:<skill>=<level>` build your hero until staff approve them.
- `+sheet/identity`, `/theme`, `/origin` and `+sheet/bond <who>=<emotions>` set your traits and bonds.
- `+sheet/bonus <bonus>=<n> <source>` adds what a skill or a piece of equipment gives, such as `+sheet/bonus def=1 Bronze shield`.
- `+sheet/hp`, `/mp`, `/ip`, `/fp`, `/status` and `/rest` keep count in play.
- Staff give experience and zenit with `+sheet/award`, and a duty can give them too. `+sheet/levelup <class>` spends 10 experience on a level, and `+sheet/buy <item>=<cost>` spends zenit. Each award and each spending is a ledger entry with its reason.
- `+sheet/ledger` lists every entry that built your sheet: the dice, class levels, skills, raises, bonuses, experience and zenit, each with where it came from. `+sheet/revoke <entry>` takes one off: your own equipment at any time, anything before approval. Staff can take off any entry, or clear a build so it starts over.

## Rolling

- `+check <attribute>+<attribute>=<difficulty>` rolls for the room, such as `+check dex+ins=hard`.
- `+check/invoke <identity|theme|origin>` and `+check/bond <bond>` spend a Fabula Point on your last check.
- `+check/support <leader>=<pair>` and `+check/group <pair>` make a group check; `+check init` rolls Initiative.

## Encounters

A fight, a chase or any scene can be an encounter with its own copy of each member's HP, MP, IP and status effects. `+encounter/start <title>` starts one and makes you its GM; `+encounter/join` takes a copy of your sheet into it. While you are in the room where it runs, damage, healing, spent IP and status effects go to that copy, so an encounter that runs for days never changes your sheet, another scene or another encounter. A room can hold several encounters, and you can be in several; `+encounter/use <n>` picks which one your commands use. When it ends, your sheet has only what the GM kept with `+encounter/keep`.

## Duties

Automated Duties roll on your own sheet, never on an encounter's copy.

---

*Rules summarised in our own words. Requires the Fabula Ultima Core Rulebook. See [[JRPG Rules License Notice|help:fabula_license_notice]].*
