// Optional real-browser smoke test. Run ONLY against a staging/provisioned PHP site.
// Usage: npm install playwright && npx playwright install chromium && DAVID_TEST_URL=https://host/showroom-glb.php node tests/browser-smoke.mjs
// This script does not assert a 60 FPS result; it collects observational metrics.
import {chromium} from 'playwright';
const url=process.env.DAVID_TEST_URL;
if(!url || !/^https?:\/\//.test(url)){console.error('Set DAVID_TEST_URL to an existing staging showroom URL.'); process.exit(2);}
const browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-angle=swiftshader']});
const page=await browser.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1});
const errors=[];page.on('pageerror',error=>errors.push(error.message));
try {
 await page.goto(url,{waitUntil:'domcontentloaded',timeout:25000});
 await page.waitForFunction(()=>window.davidDiagnostics?.().loaded,{timeout:40000});
 const startup=await page.evaluate(()=>window.davidDiagnostics());
 if(startup.selectedMeshes<300) throw Error('Expected 300+ selectable 3D meshes, saw '+startup.selectedMeshes);
 console.log('START',JSON.stringify(startup));
 const rooms=await page.locator('#rooms button').all();
 if(rooms.length!==5)throw Error('Expected five room controls');
 for(let i=0;i<5;i++){
   await rooms[i].click();await page.waitForTimeout(550);
   const state=await page.evaluate(()=>window.davidDiagnostics());
   if(state.room!==i)throw Error('Room navigation failed: expected '+i+' actual '+state.room);
   await page.screenshot({path:'room-'+(i+1)+'-webgl.png'});
   console.log('ROOM',i,state.room,state.drawCalls,state.triangles,state.fps);
 }
 await rooms[0].click();
 await page.keyboard.down('w');await page.waitForTimeout(1200);await page.keyboard.up('w');
 console.log('MOVE',JSON.stringify(await page.evaluate(()=>window.davidDiagnostics())));
 if(errors.length) throw Error('Browser errors: '+errors.join(' | '));
 console.log('PASS: GLB loaded, 5 room jumps, movement input, no page errors.');
 console.log('FPS is OBSERVATIONAL and machine-dependent; evaluate on target customer devices.');
} finally {await browser.close();}
