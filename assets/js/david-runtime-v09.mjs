/** DAVID v0.9 staging runtime utilities. Pure ESM; no THREE, DOM or network dependency.
 * This module is safe to reuse with any GLB that preserves room centers and mesh IDs.
 */
export const ROOM_Z = Object.freeze([0, 23.5, 47, 70.5, 94]);
export const ROOM_NAMES = Object.freeze([
  'Signature Guitar Gallery', 'Acoustic Hall', 'Electric Vault',
  'Brass & Woodwinds', 'Piano & Strings'
]);

export function activeRoomForZ(z, centers = ROOM_Z) {
  if (!Number.isFinite(z)) return -1;
  let best = 0;
  let distance = Infinity;
  for (let i = 0; i < centers.length; i++) {
    const d = Math.abs(z - centers[i]);
    if (d < distance) { distance = d; best = i; }
  }
  return best;
}

/** Never change group visibility, light transforms or DOM attributes every rAF.
 * This is intentionally dependency-injected to make invalidation testable in Node.
 */
export function createRoomVisibilityController({ groups, warmLights = [], buttons = [], centers = ROOM_Z }) {
  if (groups.length !== centers.length) throw new Error('Room group / center mismatch');
  let last = -1;
  let transitions = 0;
  return {
    update(z, force = false) {
      const index = activeRoomForZ(z, centers);
      if (index === -1) return -1;
      if (!force && index === last) return index;
      groups.forEach((group, k) => { group.visible = Math.abs(k - index) <= 1; });
      warmLights.forEach((light, k) => {
        light.position.z = centers[index] + (k - 1) * 6.5;
        light.intensity = index === 2 ? 18 : 23;
      });
      buttons.forEach((button, k) => button.setAttribute('aria-current', String(k === index)));
      last = index;
      transitions++;
      return index;
    },
    get lastRoom() { return last; },
    get transitions() { return transitions; }
  };
}

/** Author-approved showroom IDs come ONLY from live DB rows; mesh bindings are
 * exact identifiers + geometry-location guards. Missing or changed GLB => display only.
 * Never fill in product prices, branding, or stock from this manifest.
 */
export function productForBoundMesh(meshName, position, manifest, products) {
  if (typeof meshName !== 'string' || !meshName.startsWith('interact_')) return null;
  if (!position || !Number.isFinite(position.x) || !Number.isFinite(position.z)) return null;
  if (!Array.isArray(manifest?.bindings)) return null;
  const binding = manifest.bindings.find(entry => entry.mesh === meshName);
  if (!binding || !/^g(?:10|[1-9])$/.test(binding.slot)) return null;
  const tolerance = Math.min(.5, Math.max(0, Number(binding.tolerance_m) || 0));
  if (Math.hypot(position.x - binding.x, position.z - binding.z) > tolerance) return null;
  return products.get(binding.slot) || null;
}

export const CAMERA_PRESETS = Object.freeze([
  Object.freeze({name:'entry',      position:[0,1.75,-9], target:[0,2,5], fov:67}),
  Object.freeze({name:'left-bays',  position:[-3,1.7,-4],target:[-8.5,2.6,0],fov:65}),
  Object.freeze({name:'right-bays', position:[3,1.7,-4], target:[8.5,2.6,0], fov:65}),
  Object.freeze({name:'island',     position:[0,1.7,3.8],target:[4.1,2,.1],fov:67}),
  Object.freeze({name:'rear',       position:[0,1.7,8],  target:[0,2,-4.2],fov:75}),
]);
export function cameraPreset(room, view) {
  if (!Number.isInteger(room) || room < 0 || room >= ROOM_Z.length ||
      !Number.isInteger(view) || view < 0 || view >= CAMERA_PRESETS.length) {
    throw new RangeError('Expected room 0..4 and view 0..4');
  }
  const p = CAMERA_PRESETS[view];
  return {room, view, name:p.name, fov:p.fov,
    position:[p.position[0],p.position[1],p.position[2]+ROOM_Z[room]],
    target:[p.target[0],p.target[1],p.target[2]+ROOM_Z[room]]};
}

/** Pure, honestly labeled, elapsed-frame stats; no synthetic/estimated GPU FPS. */
export function measuredFrameStats(milliseconds) {
  const sample = [...milliseconds].filter(t => Number.isFinite(t) && t > 0).sort((a,b)=>a-b);
  if (sample.length < 10) return {samples:sample.length,medianFps:null,onePercentLowFps:null,medianMs:null,p99Ms:null};
  const medianMs=sample[Math.floor(sample.length/2)];
  const p99Ms=sample[Math.min(sample.length-1,Math.floor(sample.length*.99))];
  return {samples:sample.length,medianFps:1000/medianMs,onePercentLowFps:1000/p99Ms,medianMs,p99Ms};
}
