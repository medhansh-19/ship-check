"""Observed Discord workflow; a new session never inherits previous results."""
import json
import re
import uuid
from datetime import datetime, timezone


class Workflow:
    def __init__(self, engine):
        self.engine = engine
        with engine.db() as db:
            db.executescript("CREATE TABLE IF NOT EXISTS workflow_sessions(id TEXT PRIMARY KEY, created TEXT, data TEXT); CREATE TABLE IF NOT EXISTS workflow_messages(session TEXT,message TEXT,PRIMARY KEY(session,message));")
        if not self.state():
            self.new()

    def state(self):
        with self.engine.db() as db:
            row = db.execute("SELECT data FROM workflow_sessions ORDER BY rowid DESC LIMIT 1").fetchone()
        return json.loads(row[0]) if row else None

    def new(self):
        data = dict(id=uuid.uuid4().hex, created=datetime.now(timezone.utc).isoformat(), stages={key:"waiting" for key in ("scout","auditor","review","verify")}, activity=[], rules=[], findings=[], changes=[])
        with self.engine.db() as db:
            db.execute("INSERT INTO workflow_sessions VALUES(?,?,?)", (data["id"],data["created"],json.dumps(data)))
        return data

    def observe(self, message_id, actor, text, created=None):
        if actor not in ("owner", "scout", "auditor") or not text.strip():
            return
        with self.engine.lock:
            data = self.state()
            with self.engine.db() as db:
                if db.execute("SELECT 1 FROM workflow_messages WHERE session=? AND message=?", (data["id"],str(message_id))).fetchone():
                    return
                db.execute("INSERT INTO workflow_messages VALUES(?,?)", (data["id"],str(message_id)))
            timestamp = created or datetime.now(timezone.utc).isoformat()
            entry=dict(id=str(message_id),actor=actor,text=text[:12000],created=timestamp)
            data["activity"].append(entry)
            data["activity"]=data["activity"][-100:]
            if actor=="owner":
                if re.search(r"scout",text,re.I): data["stages"]["scout"]="working"
                if re.search(r"auditor|@audit\b",text,re.I): data["stages"]["auditor"]="working"
            elif actor=="scout":
                data["stages"]["scout"]="working"
                try:
                    from control.rules import parse_markdown
                    parsed=parse_markdown(text,"Discord message " + str(message_id))
                    existing={r["id"]:r for r in data["rules"]}
                    existing.update({r["id"]:r for r in parsed["rules"]})
                    data["rules"]=list(existing.values())
                    data["stages"]["scout"]="delivered"
                except ValueError:
                    pass
            else:
                data["stages"]["auditor"]="working"
                data["findings"].append(entry)
                data["findings"]=data["findings"][-30:]
                if re.search(r"\b(FAIL|BLOCKED|PASS|findings|numbered fixes|approve|fix list)\b",text,re.I):
                    data["stages"]["auditor"]="reported"
                    data["stages"]["review"]="needs review"
                urls=re.findall(r"https://github\.com/[^\s/]+/[^\s/]+/pull/\d+",text)
                for url in urls:
                    if url not in [c["url"] for c in data["changes"]]:data["changes"].append(dict(url=url,created=timestamp))
                if urls:data["stages"]["review"]="PR opened"
                if re.search(r"\b(retest|recheck|verification|validation|tests? passed|tests? failed)\b",text,re.I):
                    data["stages"]["verify"]="report received"
            with self.engine.db() as db:
                db.execute("UPDATE workflow_sessions SET data=? WHERE id=?", (json.dumps(data),data["id"]))
