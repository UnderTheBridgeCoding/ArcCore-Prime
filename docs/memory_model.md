Core Guarantee (Plain Language)

acOS guarantees that important moments leave durable, recoverable traces, and that active work is protected from interruption caused by LLM context loss, crashes, or resets — within a bounded, intentional memory footprint.

1. Active Context Window (≈5–8 Days)

acOS maintains a rolling active context window designed to protect ongoing work.

The base window spans approximately 5 days

Sigils increase context density, extending the window up to approximately 8 days

During this window:

Important nodes resist pruning

Relevant context may be automatically re-injected at LLM hook-in

Work can continue without re-explaining prior decisions

This window exists to prevent loss of momentum — not to guarantee permanent recall.

2. Sigils: Temporary Gravity, Durable Anchors

Sigils are intentional markers placed by the user to indicate importance.

While the active window is open:

Sigils increase memory density

Sigiled nodes are protected from premature pruning

Sigiled context is more likely to be included automatically

After the active window closes:

Sigils are no longer automatically injected

Surrounding raw context may be pruned, compressed, or externalized

The sigil marker itself persists

At this stage, sigils function as durable cognitive anchors, not payloads.

3. Intentional Reconstruction (Sigil Sweep)

If a user remembers placing a sigil, they may explicitly request reconstruction:

“Perform a sigil sweep and help reconstruct what we decided.”

In response, acOS:

Traverses sigil-marked nodes

Examines nearby structural context

Reconstructs conclusions, decisions, and meaning

Operates on available local data and compressed representations

Reconstruction is meaning-first, not verbatim replay.

4. Limits of Reconstruction (Explicit and Honest)

acOS does not guarantee perfect reconstruction in all cases.

Reconstruction quality depends on:

The amount of surrounding context retained locally

Whether raw content was compressed or externalized

The original density of the work period

Sigils guarantee recoverable traces, not complete historical playback.

This reflects how all real memory systems function — human and artificial alike.

5. Storage vs. Persistence (Critical Distinction)

Storage refers to where data physically resides (local disk, cloud, archive)

Persistence (acOS) refers to whether meaningful context can be recalled and re-injected into an LLM

acOS persistence does not require:

permanent raw transcript storage

cloud dependency

infinite context windows

acOS may compress, summarize, or transform data to preserve meaning while maintaining a light footprint.

6. Default Behavior and User Autonomy

By default:

Nodes remain locally accessible

Raw media and transcripts are not retained unless explicitly chosen

Sigils do not override user storage decisions

Users may choose to:

retain more data

externalize content

archive or compress aggressively

acOS respects autonomy while clearly communicating tradeoffs.

7. What acOS Is — and Is Not
acOS is:

a context continuity layer

a buffer against LLM memory volatility

a meaning-preserving system

a cognitive shock absorber

acOS is not:

a surveillance archive

an infinite memory vault

a replacement for provider-side data exports

a promise of eternal recall

Final Guarantee (Condensed)

acOS preserves active meaning across interruptions and ensures that important moments remain recoverable through sigil-based reconstruction — within a bounded, intentional memory model that favors continuity over hoarding.

Closing note (philosophical, but true)

Human memory fades silently and irreversibly.
acOS fades intentionally, visibly, and with recoverable anchors.
