# v0.4 GLB staging checkpoint (2026-10-11)

The v0.4 experimental build was produced in a conversation-local archive (`david-v0.4-complete-source-and-proof.zip`). It has five walkable-gallery meshes, 322 selectable instruments, 407 batched mesh nodes, and a 4,243,228-byte GLB. The generator, PHP viewer, collision module and unit tests exist in that archive, but the v0.4 GLB and source are NOT yet checked into `main`.

Checks in the producing run: structural GLB tests, Node collision unit tests, PHP syntax, isolated read-only PHP HTTP smoke, 25 VTK proof renders. Full WebGL, production database/cart integration, performance benchmarks, and photographic visual fidelity are NOT verified. Current visuals visibly fall short of the four approved reference renders.

Do not touch production PHP files, DB config, or installer until a staged preview is validated. Next: synchronize assets, test WebGL and improve realistic models/lighting.
