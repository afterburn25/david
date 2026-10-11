# DAVID approved architectural reference — do not change scope

The user selected the generated luxury instrument showroom render (October 11 2026) as the production visual target, and rejected subsequent attempts that simply hung images on walls or substituted simple geometric boxes. **Rebuild the scene as actual continuously navigable 3D geometry from multiple angles, not a panorama, billboard, wall poster, or depth-map façade.**

## Primary image: Signature Guitar Gallery (approved)
- Wide-angle eye-level view of a high-end flagship music boutique with a high ceiling, deep perspective and layered warm ambient lights.
- Left/right walls almost entirely filled with recessed, warm-backlit, dark walnut guitar bays separated by fine brass framing and lower storage cabinetry. Many red, blue, black, cream and sunburst electric guitars with recognizably precise pickups, fretboards, tuning pegs and detailed finishes.
- A central raised oval/fluted showcase with three glossy show guitars, vertical glass and slim brass supports, illuminated from above. Luxurious dark wood or black-marble architectural feature behind the showcase; a suspended cluster of slim gold pendant lights.
- Foreground left/center lounge: cognac leather sofa and armchair, woven cream/gray patterned luxury area rug, low round black-marble coffee table and ribbed brass pedestal base, textural cushions, low footstool and planters. The user specifically wants comfortable carpet/rugs and luxurious room lighting.
- Mid/back area: additional boutique acoustic section, polished reception counter, upper balcony/mezzanine impression and stepped architectural movement. No cramped tunnel or giant black blocking cubes. Depth should feel like an actual wide retail showroom.
- Material palette: espresso/walnut veneer, warm amber 3000K recessed LEDs, brushed gold/brass, smoke glass vitrines, medium-gray cream textile, cognac/dark brown leather, premium stone and subtle greenery.

## Acoustic Hall
Matching warm, sophisticated boutique; walls full of accurate acoustic and classical guitars in recessed bay lighting; maple/spruce/mahogany instruments, warm wood grain, textured wool rugs, tasteful seating and consultation table. Softer lighting than the Electric Vault.

## Electric Vault
Dark glossy premium guitar and bass gallery, wall-mounted illuminated instruments, boutique amps/effects cases, charcoal textiles, showcase hero island. Same walnut/brass brand language with slightly cooler accent contrast.

## Brass & Woodwind Gallery
Museum-quality display niches and glass cases for real saxophones, trumpets, trombones, flutes, clarinets/oboes with physically shaped keys, tubes, bells and lacquered-metal reflections. Center vitrines, lounges, warm layered lighting, Persian/wool rugs, fine cabinetry.

## Piano & Strings Salon
Visually distinctive polished full grand piano, open lid, realistic keyboard, bench, carpeted recital island. Violins, violas and cellos in wall display bays and glass cases. Elegant chairs, pendant lights and dark walnut detail.

## Fidelity and interaction acceptance
1. Actual GLB/GLTF triangle meshes and PBR materials; free walk-around/turn/inspect in 3D. Correct side and rear surfaces (not only one viewpoint).
2. All five rooms connected with usable portals, smoothly navigate from each; collision camera never clips through furnishings or walls.
3. Click instrument -> exact database-linked product info/stock if assigned. Otherwise display-only; no invented brand or prices.
4. Photo-aligned screenshots from at least five representative cameras **per room** measured against descriptions. Do not declare visual acceptance from single off-screen low-quality preview.
5. 60 FPS target on specified compatible desktops after real browser bench; adapt resolution/culling/LOD on mobile.
6. Preserve PHP/MySQL shared-host architecture. Upgrades never overwrite live database credentials, app bootstrap, installer or customer data.
7. Sources must be committed to afterburn25/david/main; update PROJECT_STATUS.md and SESSION_HANDOFF.md every milestone. Clear unverified vs completed.

## Reference availability
The four approved reference PNGs were generated in the October 11 ChatGPT project conversation and were available as temporary conversation artifacts in that session. **Their binaries are not yet in this repo**. Future sessions should request those exact existing files if visual comparison is needed; do not quietly replace them with different imagery. The descriptions here keep the direction while source images are being archived.
