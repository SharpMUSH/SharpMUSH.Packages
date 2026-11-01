A **constraint** changes how the PCs must deal with an enemy or an obstacle. Each one makes its adversary harder and more memorable, so use them sparingly.

## Countdowns

A countdown makes an adversary urgent: deal with it now, or things get worse. It is a row of boxes, one or more **triggers** that each mark a box, and an **outcome** that happens when the last box is marked. A trigger can be "an exchange elapses" or "the villain takes a consequence". A countdown can run for a scene, or for a whole campaign, as a villain's master plan.

`+countdown/start <name>=<boxes>/<outcome>` starts one, `+countdown/trigger` notes a trigger, and `+countdown/tick` marks a box for the room to see. One started in an encounter ends with it.

For example:

`+countdown/tick bomb=An exchange elapses`

Output: `[COUNTDOWN] Ticking Time Bomb moves on (An exchange elapses): [X] [ ] [ ] [ ]`

## Limitations

A limitation is a fact or an aspect that makes the obvious approach a bad idea: the werewolf is a PC's son, the mob boss is protected by powerful politicians. It does not forbid anything; it gives the players a reason to find another way. Use one or two in an adventure. On an NPC: `+npc/set <npc>/limit=<limitation>`.

## Resistances

A resistance forbids a course of action, with one way through. Its **lock** is an aspect saying what the adversary is immune to; its **key** is the one thing that gets past it. Getting the key is often an adventure in itself. Have one in play at a time.

- The Dragon. Lock: *Immune to Mortal Weaponry*. Key: The Sword of Avelah, created by an immortal race long ago, can harm the dragon.
- The Alien. Lock: *Doesn't Understand Earthly Communication*. Key: Emily Jace, the only survivor from a deep-space expedition, is the only human known to have learned the alien language.
- The Wall. Lock: *Unnaturally Smooth, Can't Be Climbed*. Key: If you can get a device that'll vibrate at the right harmonic frequency, you can walk right through the wall.

On an obstacle, `+obstacle/lock <obstacle>=<lock>/<key>` sets one, and no roll gets past it until the GM clears it. On an NPC: `+npc/set <npc>/lock=<lock>` and `+npc/set <npc>/key=<key>`.

---

*Rules based on the Fate Adversary Toolkit SRD under CC BY 3.0. An unofficial fan package. See [[Fate Adversary Toolkit License Notice|help:fate_adversary_toolkit_license_notice]].*
