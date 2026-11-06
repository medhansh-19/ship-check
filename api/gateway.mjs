import {timingSafeEqual} from 'node:crypto';

export function equalSecret(value,expected){
  if(!value||!expected)return false;
  const a=Buffer.from(value),b=Buffer.from(expected);
  return a.length===b.length&&timingSafeEqual(a,b);
}

export default async function handler(req,res){
  res.setHeader('Cache-Control','no-store');
  const action=req.query?.action;
  const writes=new Set(['audit','decision','pr','checklist','rule-review']);
  const read=req.method==='GET'&&action==='state';
  if(!read&&!(req.method==='POST'&&writes.has(action)))return res.status(404).json({error:'Not found'});
  if(!read&&!equalSecret(req.headers['x-ship-check-owner'],process.env.SHIP_CHECK_OWNER_KEY))return res.status(401).json({error:'Owner access required. Use Unlock owner controls and enter your owner key.'});
  if(!read){
    const origin=req.headers.origin;
    if(origin&&new URL(origin).host!==req.headers.host)return res.status(403).json({error:'Cross-origin writes are not allowed.'});
  }
  const backend=process.env.SHIP_CHECK_BACKEND_URL;
  const relay=process.env.SHIP_CHECK_RELAY_SECRET;
  if(!backend||!relay)return res.status(503).json({error:'The audit runner is not configured.'});
  try{
    const url=new URL('/api/relay/'+action,backend);
    if(url.protocol!=='https:'&&process.env.NODE_ENV!=='test')throw new Error('HTTPS required');
    const body=read?undefined:JSON.stringify(req.body||{});
    if(body&&Buffer.byteLength(body)>16384)return res.status(413).json({error:'Request is too large.'});
    const upstream=await fetch(url,{method:req.method,headers:{'Authorization':'Bearer '+relay,'Content-Type':'application/json'},body,signal:AbortSignal.timeout(action==='pr'?110000:20000),redirect:'error'});
    const result=await upstream.json();
    if(read&&upstream.ok){
      delete result.csrf;
      result.csrf='hosted';
      result.hosted=true;
      result.owner_unlocked=equalSecret(req.headers['x-ship-check-owner'],process.env.SHIP_CHECK_OWNER_KEY);
      return res.status(200).json(result);
    }
    return res.status(upstream.status).json(result);
  }catch{
    return res.status(503).json({error:'Audit runner is offline. Keep the Ship Check service and secure tunnel running on the owner’s Mac.'});
  }
}
