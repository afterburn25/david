<?php
/**
 * DAVID optional GLB showroom. Copy this file to the installed website root.
 * Read-only on load; sends a validated add-to-cart request only on an explicit click.
 * Does not run installer, change configuration, or modify database schema.
 */
require __DIR__.'/app/bootstrap.php';
require_install();
$rows=db()->query("SELECT id,showroom_id,brand,name,description,category,price_cents,stock,status FROM products WHERE showroom_id IS NOT NULL AND status IN ('active','demo') ORDER BY id LIMIT 500")->fetchAll(PDO::FETCH_ASSOC);
$catalog=[];
foreach ($rows as $r) {
    $catalog[]=['id'=>(int)$r['id'],'slot'=>(string)$r['showroom_id'], 'brand'=>(string)$r['brand'], 'name'=>(string)$r['name'], 'description'=>(string)$r['description'], 'category'=>(string)$r['category'], 'price'=>(int)$r['price_cents']/100, 'stock'=>(int)$r['stock'], 'status'=>(string)$r['status']];
}
$csrf=csrf();
?><!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prof Erny's Music — Luxury 3D Gallery</title>
<style>
:root{color-scheme:dark;--gold:#e6bd7e;--text:#f5ede0;--ink:#140f0d}*{box-sizing:border-box}html,body{height:100%;margin:0;overflow:hidden;background:#100d0b;color:var(--text);font-family:Inter,system-ui,sans-serif}button,a{font:inherit}button{cursor:pointer}.ui{position:fixed;z-index:3;background:#1a1512e6;border:1px solid #9a775293;border-radius:13px;backdrop-filter:blur(15px)}header{top:15px;left:18px;right:18px;padding:15px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px}header strong{font-family:Georgia,serif;letter-spacing:.07em;font-size:18px}header a,aside a{color:var(--gold)}nav{left:18px;top:86px;width:214px;padding:14px}nav h2{font-size:10px;letter-spacing:.18em;color:#c9b298;margin:0 0 9px}nav button{display:block;text-align:left;margin:5px 0;padding:11px;border:1px solid #77583d;background:#271f19;color:#fff0df;border-radius:7px;width:100%}nav button[aria-current="true"]{background:#755130;border-color:#f2c78c}nav button:hover{background:#4e3527}#perf{left:18px;bottom:15px;padding:11px;font-size:12px;color:#e9cc9f}#help{bottom:15px;right:18px;padding:11px;font-size:12px;color:#d3c3ab}#info{top:86px;right:18px;width:min(355px,calc(100vw - 36px));padding:18px;display:none;box-shadow:0 15px 65px #0009}#info h2{font-family:Georgia,serif;font-size:25px;font-weight:400;margin:8px 0}#info p{font-size:13px;color:#ddcdb9;line-height:1.6}#info small{color:#e3bb82}#info .price{font-size:22px;color:#ffe0af;font-weight:750}#info button{background:#ca9d60;color:#1d1109;border:0;padding:11px 13px;border-radius:8px;margin:5px 0;width:100%;font-weight:650}#info button:disabled{opacity:.4;cursor:not-allowed}#info button.secondary{background:#37271b;color:#fff0d2;border:1px solid #866243}#info a{display:block;text-align:center;padding:10px;color:#ecc593}#view{position:fixed;inset:0}#view canvas{display:block;touch-action:none}#loading{position:fixed;z-index:5;inset:0;background:#110e0d;display:flex;align-items:center;justify-content:center;color:#ffdfaa;text-align:center;padding:20px}#minimap{display:none}#mobile{display:none;z-index:5;position:fixed;bottom:65px;right:12px;grid-template-columns:repeat(3,45px);gap:5px}#mobile button{background:#32241dcf;border:1px solid #b79264;border-radius:8px;color:#fff7e6;font-size:20px;height:44px;touch-action:none}#mobile .blank{visibility:hidden}@media(max-width:750px){header{left:8px;right:8px;top:7px;padding:11px}header strong{font-size:13px}header a{font-size:11px}nav{left:8px;top:69px;width:157px;padding:8px}nav button{font-size:11px;padding:8px}#help{display:none}#mobile{display:grid}#info{top:69px;right:8px}#perf{left:8px;bottom:8px} }
</style>
<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.163.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.163.0/examples/jsm/"}}</script></head><body>
<div id="loading">Loading the 3D galleries…</div><div id="view"></div>
<header class="ui"><strong>PROF ERNY'S <span style="color:var(--gold)">MUSIC</span> · 3D</strong><div><a href="index.php">Original showroom</a> &nbsp;·&nbsp; <a href="catalog.php">Shop catalog</a> &nbsp;·&nbsp; <a href="cart.php">Bag</a></div></header>
<nav class="ui"><h2>EXPLORE THE GALLERIES</h2><div id="rooms"></div><h2 style="margin-top:13px">PERFORMANCE</h2><button id="quality">Quality: Auto</button></nav>
<div id="perf" class="ui" aria-live="off">GLB: loading · FPS: --</div><div id="help" class="ui">WASD walk · Drag look · Click instruments · ESC close</div>
<aside class="ui" id="info" role="dialog" aria-label="Instrument details"><small id="roomName">3D EXHIBIT</small><h2 id="itemName"></h2><p id="itemDesc"></p><div class="price" id="itemPrice"></div><button id="add" disabled>Add to live bag</button><button class="secondary" id="inspect">Inspect up close</button><button class="secondary" id="close">Back to gallery</button><a href="catalog.php">Browse verified inventory</a></aside>
<div id="mobile"><span class="blank"></span><button data-key="w">↑</button><span class="blank"></span><button data-key="a">←</button><button data-key="s">↓</button><button data-key="d">→</button></div>
<script type="module">
import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
const catalog=<?=json_encode($catalog,JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT)?>;
const csrf=<?=json_encode($csrf,JSON_HEX_TAG|JSON_HEX_AMP|JSON_HEX_APOS|JSON_HEX_QUOT)?>;
const products=new Map(catalog.map(p=>[p.slot,p]));
const rooms=[['Signature Guitar Gallery',0],['Acoustic Hall',23.5],['Electric Vault',47],['Brass & Woodwinds',70.5],['Piano & Strings',94]];
const $=s=>document.querySelector(s);
const scene=new THREE.Scene(); scene.background=new THREE.Color('#120c09');scene.fog=new THREE.FogExp2(0x22130e,.006);
scene.add(new THREE.HemisphereLight(0xffe9ce,0x47311c,2.1));
const amb=new THREE.DirectionalLight(0xffc891,2.3);amb.position.set(-5,7,-3);scene.add(amb);
const warmLights=[];
for(let i=0;i<3;i++){
 const l=new THREE.PointLight(0xffb56d,18,14,2);l.position.set(i===0?-7:i===1?1:7,4,0);scene.add(l);warmLights.push(l);
}
const camera=new THREE.PerspectiveCamera(67,innerWidth/innerHeight,.10,170);camera.position.set(0,1.73,-9);camera.rotation.order='YXZ';
const renderer=new THREE.WebGLRenderer({antialias:true,powerPreference:'high-performance',alpha:false});
renderer.setSize(innerWidth,innerHeight);renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.68;
$('#view').append(renderer.domElement);
const controls={yaw:Math.PI,goalYaw:Math.PI,pitch:-.01,goalPitch:-.01};const keys=new Set();const vel=new THREE.Vector3();
const GROUPS=rooms.map(()=>new THREE.Group());GROUPS.forEach(g=>scene.add(g));
let currentRoom=0,selectable=[],selected=null,savedView=null,inspecting=false,qualityMode=0,scale=1,loaded=false;
const ray=new THREE.Raycaster();const mpos=new THREE.Vector2();
function dpr(){return Math.min(devicePixelRatio,scale)}
function applyQuality(){renderer.setPixelRatio(dpr());renderer.setSize(innerWidth,innerHeight,false);$('#quality').textContent='Quality: '+['Auto','Performance','Balanced','High'][qualityMode]}
function setRoom(i){currentRoom=i;camera.position.set(0,1.73,rooms[i][1]-8);controls.goalYaw=Math.PI;controls.yaw=Math.PI;controls.pitch=controls.goalPitch=-.01;vel.set(0,0,0);setPanel(false);updateSceneVisibility();document.querySelectorAll('#rooms button').forEach((b,k)=>b.setAttribute('aria-current',String(k===i)))}
rooms.forEach(([name,z],i)=>{const btn=document.createElement('button');btn.textContent=(i+1)+'. '+name;btn.onclick=()=>setRoom(i);$('#rooms').append(btn)});
$('#quality').onclick=()=>{qualityMode=(qualityMode+1)%4;scale=[Math.min(devicePixelRatio,1.15),.72,1.05,1.6][qualityMode];applyQuality()};
scale=Math.min(1.15,devicePixelRatio);applyQuality();
function roomFromName(name){const a=/^room_(\d+)__/.exec(name);if(a)return Number(a[1]);const b=/^interact_(\d+)_/.exec(name);return b?Number(b[1]):-1}
function updateSceneVisibility(){let idx=Math.max(0,Math.min(4,Math.floor((camera.position.z+11.75)/23.5)));currentRoom=idx;GROUPS.forEach((g,k)=>g.visible=Math.abs(k-idx)<=1);warmLights.forEach((l,k)=>{l.position.z=rooms[idx][1]+(k-1)*6.5;l.intensity=idx===2?18:23});document.querySelectorAll('#rooms button').forEach((b,k)=>b.setAttribute('aria-current',String(k===idx)))}
new GLTFLoader().load('assets/rooms/luxury-showroom-v03-optimized.glb',g=>{
 const objs=[];g.scene.traverse(o=>{if(o.isMesh)objs.push(o)});
 for(const o of objs){const idx=roomFromName(o.name);if(idx>=0){o.parent.remove(o);GROUPS[idx].add(o)}if(o.name.startsWith('interact_'))selectable.push(o)}
 loaded=true;$('#loading').remove();updateSceneVisibility();
 $('#perf').textContent='3D loaded · '+selectable.length+' selectable meshes · FPS: --';
},undefined,e=>{$('#loading').textContent='3D model failed to load. '+e.message+' — Verify assets/rooms/ is uploaded.'});
function setPanel(visible){$('#info').style.display=visible?'block':'none';if(!visible){selected=null;if(savedView){camera.position.copy(savedView.pos);controls.goalYaw=savedView.yaw;controls.goalPitch=savedView.pitch;savedView=null;inspecting=false}}}
function productForPick(obj){let m=/^interact_(\d+)_(\d+)/.exec(obj.name);if(!m)return null;let room=Number(m[1]),slot=Number(m[2]);
 // Never mislabel an exhibit with a random product. Link only known admin-assigned showroom IDs.
 let key=(room===0&&slot<10)?'g'+(slot+1):null;
 return key?products.get(key)||null:null;
}
function openProduct(hit){selected=hit;const pm=/^interact_(\d+)_(\d+)_(.+)/.exec(hit.name);
 const room=pm?Number(pm[1]):currentRoom;const product=productForPick(hit);
 $('#roomName').textContent=rooms[room][0].toUpperCase();
 $('#itemName').textContent=product?product.brand+' '+product.name:({guitar:'Guitar showcase',violin:'Strings exhibit',sax:'Brass & woodwind exhibit',grand_piano:'Grand piano'}[pm?.[3]]||'3D Instrument Exhibit');
 $('#itemDesc').textContent=product?product.description:'This is an architecturally modeled showroom exhibit. No live brand, price or stock is assigned to this individual model yet. Use the catalog for verified inventory.';
 $('#itemPrice').textContent=product&&product.status==='active'?new Intl.NumberFormat('en-US',{style:'currency',currency:'USD'}).format(product.price):'DISPLAY ONLY';
 $('#add').disabled=!(product?.status==='active'&&product.stock>0);
 $('#add').onclick=async()=>{if(!product)return;const body=new FormData();body.set('csrf',csrf);body.set('action','add');body.set('id',String(product.id));try{const r=await fetch('cart.php',{method:'POST',body,headers:{Accept:'application/json'}});const d=await r.json();if(!r.ok||!d.ok)throw Error('Cart update failed');$('#add').textContent='Added — View Bag';$('#add').onclick=()=>location.assign('cart.php')}catch(err){$('#itemDesc').textContent='Could not update your bag. Please try the catalog.'}};
 $('#info').style.display='block';
}
$('#close').onclick=()=>setPanel(false);$('#inspect').onclick=()=>{
 if(!selected)return;
 if(savedView){setPanel(false);return}
 savedView={pos:camera.position.clone(),yaw:controls.goalYaw,pitch:controls.goalPitch};inspecting=true;
 const bounds=new THREE.Box3().setFromObject(selected);const c=bounds.getCenter(new THREE.Vector3());let offset;
 // Wall instruments face inward, so approach from center aisle not through the display wall.
 if(Math.abs(c.x)>7)offset=new THREE.Vector3(c.x<0?2.1:-2.1,0,0);else offset=new THREE.Vector3(0,0,-2.8);
 const dest=c.clone().add(offset);dest.y=1.75;camera.position.copy(dest);
 const dv=c.clone().sub(camera.position);controls.goalYaw=Math.atan2(-dv.x,-dv.z);controls.yaw=controls.goalYaw;controls.goalPitch=Math.max(-.7,Math.min(.7,Math.atan2(dv.y,Math.hypot(dv.x,dv.z))));
 $('#inspect').textContent='Return from close-up';
};
renderer.domElement.addEventListener('pointerdown',e=>{renderer.domElement.setPointerCapture(e.pointerId);renderer.domElement.dataset.pointerX=e.clientX;renderer.domElement.dataset.pointerY=e.clientY;renderer.domElement.dataset.moved='false'});
renderer.domElement.addEventListener('pointermove',e=>{if(!renderer.domElement.hasPointerCapture(e.pointerId))return;const x=Number(renderer.domElement.dataset.pointerX),y=Number(renderer.domElement.dataset.pointerY),dx=e.clientX-x,dy=e.clientY-y;if(Math.abs(dx)+Math.abs(dy)>2)renderer.domElement.dataset.moved='true';controls.goalYaw-=dx*.0025;controls.goalPitch=Math.max(-1.3,Math.min(1.3,controls.goalPitch-dy*.0024));renderer.domElement.dataset.pointerX=e.clientX;renderer.domElement.dataset.pointerY=e.clientY});
renderer.domElement.addEventListener('pointerup',e=>{if(renderer.domElement.dataset.moved==='true')return;mpos.set((e.clientX/innerWidth)*2-1,-(e.clientY/innerHeight)*2+1);ray.setFromCamera(mpos,camera);const hits=ray.intersectObjects(selectable,false);if(hits.length)openProduct(hits[0].object)});
window.addEventListener('keydown',e=>{const k=e.key.toLowerCase();if(['w','a','s','d','arrowup','arrowdown','arrowleft','arrowright',' '].includes(k))e.preventDefault();if(k==='escape')setPanel(false);keys.add(k)});window.addEventListener('keyup',e=>keys.delete(e.key.toLowerCase()));window.addEventListener('blur',()=>keys.clear());
for(const b of document.querySelectorAll('#mobile button')){const k=b.dataset.key;b.addEventListener('pointerdown',e=>{e.preventDefault();keys.add(k);b.setPointerCapture(e.pointerId)});for(const ev of ['pointerup','pointercancel'])b.addEventListener(ev,()=>keys.delete(k))}
const solids=rooms.flatMap(([n,z])=>[{x1:-5.3,x2:-1.0,z1:z-3.25,z2:z-1.5},{x1:2.0,x2:6.25,z1:z-1.6,z2:z+1.8}]);
function freeSpot(x,z){if(Math.abs(x)>8.45||z < -10.5||z>103.5)return false;
 for(const [,center] of rooms.slice(0,4)){let portal=center+11.72;if(Math.abs(z-portal)<.40&&Math.abs(x)>2.3)return false}
 return !solids.some(s=>x>s.x1-.35&&x<s.x2+.35&&z>s.z1-.35&&z<s.z2+.35)}
let previous=performance.now(),sum=0,frames=0,lastAuto=0,fps=0;
function frame(now){requestAnimationFrame(frame);const dt=Math.min((now-previous)/1000,.045);previous=now;
 const blend=1-Math.exp(-13*dt);controls.yaw+=(controls.goalYaw-controls.yaw)*blend;controls.pitch+=(controls.goalPitch-controls.pitch)*blend;camera.rotation.set(controls.pitch,controls.yaw,0,'YXZ');
 if(!selected){let fw=(keys.has('w')||keys.has('arrowup')?1:0)-(keys.has('s')||keys.has('arrowdown')?1:0);let st=(keys.has('d')||keys.has('arrowright')?1:0)-(keys.has('a')||keys.has('arrowleft')?1:0);let n=Math.max(1,Math.hypot(fw,st));let speed=keys.has('shift')?5.4:3.4;const x=(-Math.sin(controls.yaw)*fw+Math.cos(controls.yaw)*st)*speed/n,z=(-Math.cos(controls.yaw)*fw-Math.sin(controls.yaw)*st)*speed/n;vel.x+=(x-vel.x)*(1-Math.exp(-9*dt));vel.z+=(z-vel.z)*(1-Math.exp(-9*dt));let nx=camera.position.x+vel.x*dt,nz=camera.position.z+vel.z*dt;
 if(freeSpot(nx,camera.position.z))camera.position.x=nx;else vel.x=0;
 if(freeSpot(camera.position.x,nz))camera.position.z=nz;else vel.z=0;
 }
 if(loaded)updateSceneVisibility();renderer.render(scene,camera);
 frames++;sum+=dt;if(sum>=1){fps=frames/sum;$('#perf').textContent=`GLB ${selectable.length} picks · ${Math.round(fps)} FPS · ${Math.round(dpr()*100)}% render`;
 if(qualityMode===0&&now-lastAuto>3200){if(fps<51&&scale>.7)scale-=.10;else if(fps>59&&scale<Math.min(1.5,devicePixelRatio))scale+=.045;scale=Math.max(.7,Math.min(scale,1.5));applyQuality();lastAuto=now}frames=0;sum=0}
}
window.addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();applyQuality()});
// Lightweight debug surface for screenshot testing; no secrets or personal data.
window.davidDiagnostics=()=>({loaded,selectedMeshes:selectable.length,room:currentRoom,fps:Math.round(fps),drawCalls:renderer.info.render.calls,triangles:renderer.info.render.triangles,qualityMode});
requestAnimationFrame(frame);
</script></body></html>