"""Turn Scout's quoted Markdown checklist into data, never executable instructions."""
import re
from pathlib import Path


def available(repo):
    root = Path(repo).resolve()
    return [str(p.relative_to(root)) for p in sorted((root / "scout/checklists").glob("*.md")) if p.name != "README.md" and not p.is_symlink()]


def parse_markdown(text, path):
    source = re.search(r"(?im)^- Primary source:\s*(https?://\S+)", text)
    event = re.search(r"(?m)^# (.+)", text)
    heading = "Requirements"
    rules = []
    matches = list(re.finditer(r"(?m)^- \[[ xX]\] \*\*(.+?)\*\*", text))
    seen = set()
    for index, match in enumerate(matches):
        label = match.group(1)
        identifier = label.split(" — ")[0].strip()
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{1,80}", identifier):
            raise ValueError("Every checklist item needs a stable ID before its first em dash.")
        if identifier in seen:
            raise ValueError("Duplicate checklist ID: " + identifier)
        seen.add(identifier)
        preceding = list(re.finditer(r"(?m)^## (.+)", text[:match.start()]))
        if preceding:
            heading = preceding[-1].group(1)
        body = text[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        # Quotes are preserved; checked Markdown boxes are not trusted proof.
        quote = "\n".join(re.findall(r"(?m)^\s*> ?(.*)$", body)).strip()
        location = re.search(r"(?m)^\s*Source:\s*(.+)", body)
        optional = bool(re.search(r"\bOPTIONAL\b", label, re.I))
        mandatory = bool(re.search(r"\bMUST\b", label)) and not optional
        conditional = mandatory and bool(re.search(r"only if|only for|conditional|optional prizes", label + " " + heading, re.I))
        rules.append(dict(id="event:" + identifier, title=label, status="needs_review", evidence="Source requirement imported. Human evidence is required." if quote else "Scout did not include a source quote. Resolve this before verification.", proposal=None, category=heading, requirement="optional" if optional else "conditional" if conditional else "mandatory" if mandatory else "review", source=source.group(1) if source else None, location=location.group(1).strip() if location else path, quote=quote, checklist=path, scored=mandatory and not conditional, verifier="human"))
    if not rules:
        raise ValueError("No stable, quoted Scout checklist items were found.")
    return dict(name=event.group(1) if event else Path(path).stem, source=source.group(1) if source else None, checklist=path, rules=rules)


def load(repo, selected):
    if not selected:
        return None
    root = Path(repo).resolve()
    path = root / selected
    if selected not in available(root) or not path.resolve().is_relative_to(root):
        raise ValueError("Select a Scout checklist from scout/checklists/.")
    return parse_markdown(path.read_text(), selected)
