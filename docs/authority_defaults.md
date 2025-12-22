Authority Scale (Default)
0 → Passive / Read-only
1 → Normal interaction (default user & LLM)
3 → Marking intent (sigils, priority)
5 → Semantic reshaping (compression changes)
7 → Structural mutation (collapse, prune)
9 → System governance / recovery


This scale is:

monotonic

sparse (room to grow)

explainable to humans

Default Actor Authority
Actor	Authority	Rationale
Normal user interaction	1	Writing memory should “just work”
Normal LLM response	1	Same as user; no silent escalation
System ingestion routines	3	Allowed to mark but not govern
Recovery / migration tools	9	Explicit, rare, auditable

👉 Default actor_authority = 1

This is the most important decision.
It prevents Sentinel from “randomly blocking” normal use.

Default Node Authority
Node Type	Authority
Fresh RAW node	0
SUMMARY node	1
SEED node	3
SIGIL_ONLY node	5

Meaning:

The more compressed / anchored, the harder it is to mutate

Reading is always allowed

Writing around is allowed

Marking over requires intent

Default Cycle Authority

Simple, non-magical rule:

cycle_authority = min(cycle_id, 5)


Examples:

Cycle 1 → authority 1

Cycle 3 → authority 3

Cycle 12 → authority 5 (cap)

This avoids:

infinite escalation

late-cycle brittleness

Default Sigil Authority

Each sigil increases authority by +2, capped.

sigil_authority = min(2 * sigil_count, 5)


Meaning:

One sigil matters

Three sigils is “hands off”

You never need infinite authority

2️⃣ Where These Defaults Live (Important)

Do NOT hardcode these into Sentinel.

They belong in one place only:

docs/AUTHORITY_DEFAULTS.md


And optionally mirrored as constants in:

ac_authority_defaults.py

Why this matters

Sentinel stays pure

Authority is policy, not mechanism

Users can change these without touching logic

Codex cannot “reinterpret” numbers later

What goes in AUTHORITY_DEFAULTS.md

The table above

The formulas (cycle cap, sigil multiplier)

Explicit statement: “These are defaults, not law”

That’s it.

3️⃣ Mapping Guardian Under Sentinel (Conceptual Only)

You asked to stop after mapping, so here is the final conceptual alignment.

Guardian’s Role (after Loop 3)

Guardian becomes a pre-Sentinel semantic filter.

Guardian answers:

“Is this content allowed?”

“Is this role permitted?”

“Is this structurally valid?”

Sentinel answers:

“Is this action authorized?”

They do not overlap.

Mapping Table
Guardian Check	Sentinel Equivalent
purify()	❌ (Guardian-only)
role validation	❌ (Guardian-only)
depth / recursion safety	❌ (Guardian-only)
content filtering	❌ (Guardian-only)
memory mutation permission	✅ Sentinel
sigil application permission	✅ Sentinel
compression change permission	✅ Sentinel
prune / collapse	✅ Sentinel

Guardian never decides authority.
Sentinel never inspects content.
