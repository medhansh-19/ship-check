import {mkdir,copyFile} from 'node:fs/promises';
await mkdir('public',{recursive:true});
for(const name of ['index.html','style.css','app.js'])await copyFile('control/static/'+name,'public/'+name);
console.log('Built Ship Check dashboard. No repository data or credentials bundled.');
