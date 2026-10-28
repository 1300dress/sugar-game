"""Keep the game's lines in step between Notion and this repo, both ways.

Source of truth for every line, in both languages: script/scenes/*.json
(one file per scene, one entry per line, keyed by Line ID). The same
lines live in the Notion SCRIPT page (Scenes and Lines databases).
The game itself still reads data/*.json; `build` writes those from the
scene files.

  python3 tools/script_sync.py sync       # both ways, then build
  python3 tools/script_sync.py status     # what sync would do, no writes
  python3 tools/script_sync.py build      # scene files -> data/*.json
  python3 tools/script_sync.py sync --prefer notion   # settle conflicts

How `sync` decides, line by line: script/.sync_state.json keeps a hash
of each line as it was after the last sync. A side that still matches
that hash has not been touched, so the other side's version wins. If
both sides changed, it is a conflict: nothing is written for that line
until it is settled with --prefer notion|repo.

Needs NOTION_TOKEN in .env at the repo root (see .env.example). The
Notion integration must be connected to the SCRIPT page.
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SCENES_DIR = os.path.join(ROOT, "script", "scenes")
STATE_FILE = os.path.join(ROOT, "script", ".sync_state.json")

NOTION_VERSION = "2022-06-28"
# SCRIPT — 대사·나레이션 (under SUGAR / HONEY / ICED TEA)
DEFAULT_LINES_DB = "9ee5b517ae204903855a9d84901de225"
DEFAULT_SCENES_DB = "e65a1e1416454e3b92921c3469ff5a17"
WRITE_PAUSE = 0.35   # s between Notion writes (limit is ~3 requests/s)

# the fields that make up a line, and the Notion property each maps to
LINE_FIELDS = {
    "scene": "씬",
    "order": "순번",
    "type": "타입",
    "speaker": "화자",
    "group": "그룹",
    "set": "세트",
    "ko": "한국어",
    "en": "English",
    "note": "연출 메모",
    "ko_status": "KO 상태",
    "en_status": "EN 상태",
}
SCENE_FIELDS = {
    "title": "씬 제목",
    "chapter": "챕터",
    "order": "순서",
    "place": "장소",
    "summary": "요약",
    "status": "상태",
}
NUMBER_PROPS = {"순번", "세트", "순서"}
SELECT_PROPS = {"타입", "화자", "그룹", "KO 상태", "EN 상태", "챕터"}
STATUS_PROPS = {"상태"}
TEXT_PROPS = {"한국어", "English", "연출 메모", "장소", "요약", "Scene ID"}


# --------------------------------------------------
# repo side
# --------------------------------------------------

def load_env():
    env = {}
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for row in open(path, encoding="utf-8"):
            row = row.strip()
            if row and not row.startswith("#") and "=" in row:
                k, v = row.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    env.update({k: v for k, v in os.environ.items() if k.startswith("NOTION_")})
    return env


def read_scene_files():
    """{scene_id: {"scene": {...}, "target": {...}, "lines": [...]}}"""
    out = {}
    if not os.path.isdir(SCENES_DIR):
        return out
    for name in sorted(os.listdir(SCENES_DIR)):
        if name.endswith(".json"):
            doc = json.load(open(os.path.join(SCENES_DIR, name), encoding="utf-8"))
            out[doc["scene"]["id"]] = doc
    return out


def write_scene_file(doc):
    doc["lines"].sort(key=lambda l: (l.get("group") or "", l.get("set") or 0,
                                     l.get("order") or 0, l["id"]))
    path = os.path.join(SCENES_DIR, doc["scene"]["id"] + ".json")
    os.makedirs(SCENES_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")


def repo_records(docs):
    """Flatten scene files to {key: record}; keys are 'scene:ID' / 'line:ID'."""
    recs = {}
    for sid, doc in docs.items():
        recs["scene:" + sid] = {f: doc["scene"].get(f) for f in SCENE_FIELDS}
        for line in doc["lines"]:
            rec = {f: line.get(f) for f in LINE_FIELDS}
            rec["scene"] = sid
            recs["line:" + line["id"]] = rec
    return recs


def apply_to_repo(docs, key, rec):
    """Write one record (or None to delete it) into the scene files in memory."""
    kind, ident = key.split(":", 1)
    if kind == "scene":
        if rec is None:
            docs.pop(ident, None)
            path = os.path.join(SCENES_DIR, ident + ".json")
            if os.path.exists(path):
                os.remove(path)
            return
        doc = docs.setdefault(ident, {"scene": {"id": ident}, "target": None, "lines": []})
        doc["scene"].update(rec)
        return
    for doc in docs.values():
        doc["lines"] = [l for l in doc["lines"] if l["id"] != ident]
    if rec is not None:
        sid = rec["scene"]
        doc = docs.setdefault(sid, {"scene": {"id": sid}, "target": None, "lines": []})
        line = {"id": ident}
        line.update({f: rec.get(f) for f in LINE_FIELDS if f != "scene"})
        doc["lines"].append(line)


# --------------------------------------------------
# Notion side
# --------------------------------------------------

class Notion:
    def __init__(self, token):
        self.token = token

    def call(self, method, path, body=None):
        req = urllib.request.Request(
            "https://api.notion.com/v1/" + path, method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={"Authorization": "Bearer " + self.token,
                     "Notion-Version": NOTION_VERSION,
                     "Content-Type": "application/json"})
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                if e.code == 429 or e.code >= 500:
                    time.sleep(float(e.headers.get("Retry-After", 1 + attempt)))
                    continue
                sys.exit(f"Notion {method} {path}: {e.code} {e.read().decode()[:300]}")
        sys.exit(f"Notion {method} {path}: gave up after retries")

    def query(self, db):
        rows, cursor = [], None
        while True:
            body = {"page_size": 100}
            if cursor:
                body["start_cursor"] = cursor
            r = self.call("POST", f"databases/{db}/query", body)
            rows += r["results"]
            if not r.get("has_more"):
                return rows
            cursor = r["next_cursor"]

    def create(self, db, props):
        time.sleep(WRITE_PAUSE)
        return self.call("POST", "pages", {"parent": {"database_id": db}, "properties": props})

    def update(self, page_id, props):
        time.sleep(WRITE_PAUSE)
        return self.call("PATCH", f"pages/{page_id}", {"properties": props})

    def archive(self, page_id):
        time.sleep(WRITE_PAUSE)
        return self.call("PATCH", f"pages/{page_id}", {"archived": True})


def plain(rich):
    return "".join(t.get("plain_text", "") for t in rich) or None


def read_prop(p):
    if p is None:   # property removed or renamed in Notion
        return None
    t = p["type"]
    if t == "title":
        return plain(p["title"])
    if t == "rich_text":
        return plain(p["rich_text"])
    if t == "number":
        n = p["number"]
        return int(n) if isinstance(n, float) and n.is_integer() else n
    if t in ("select", "status"):
        return p[t]["name"] if p[t] else None
    if t == "relation":
        return [r["id"] for r in p["relation"]]
    return None


def write_prop(name, value):
    if name in NUMBER_PROPS:
        return {"number": value}
    if name in SELECT_PROPS:
        return {"select": {"name": value} if value else None}
    if name in STATUS_PROPS:
        return {"status": {"name": value} if value else None}
    if name in TEXT_PROPS:
        return {"rich_text": [{"text": {"content": value}}] if value else []}
    raise KeyError(name)


def notion_records(client, lines_db, scenes_db):
    """Returns {key: record} plus {key: page_id} and {scene_id: page_id}."""
    recs, pages, scene_pages = {}, {}, {}
    scene_of_page = {}
    for row in client.query(scenes_db):
        p = row["properties"]
        sid = read_prop(p.get("Scene ID"))
        if not sid:
            continue
        rec = {f: read_prop(p.get(n)) for f, n in SCENE_FIELDS.items()}
        recs["scene:" + sid] = rec
        pages["scene:" + sid] = row["id"]
        scene_pages[sid] = row["id"]
        scene_of_page[row["id"].replace("-", "")] = sid
    for row in client.query(lines_db):
        p = row["properties"]
        lid = read_prop(p.get("Line ID"))
        if not lid:
            continue
        rec = {}
        for f, n in LINE_FIELDS.items():
            v = read_prop(p.get(n))
            if f == "scene":
                v = scene_of_page.get(v[0].replace("-", "")) if v else None
            rec[f] = v
        recs["line:" + lid] = rec
        pages["line:" + lid] = row["id"]
    return recs, pages, scene_pages


def push_one(client, dbs, pages, scene_pages, key, rec):
    kind, ident = key.split(":", 1)
    if rec is None:
        client.archive(pages[key])
        return
    if kind == "scene":
        props = {"씬 제목": {"title": [{"text": {"content": rec.get("title") or ident}}]},
                 "Scene ID": write_prop("Scene ID", ident)}
        props.update({n: write_prop(n, rec.get(f)) for f, n in SCENE_FIELDS.items() if f != "title"})
        db = dbs["scenes"]
    else:
        props = {"Line ID": {"title": [{"text": {"content": ident}}]},
                 "씬": {"relation": [{"id": scene_pages[rec["scene"]]}] if rec.get("scene") in scene_pages else []}}
        props.update({n: write_prop(n, rec.get(f)) for f, n in LINE_FIELDS.items() if f != "scene"})
        db = dbs["lines"]
    if key in pages:
        client.update(pages[key], props)
    else:
        page = client.create(db, props)
        pages[key] = page["id"]
        if kind == "scene":
            scene_pages[ident] = page["id"]


# --------------------------------------------------
# reconcile
# --------------------------------------------------

def digest(rec):
    if rec is None:
        return None
    # an empty string and a missing value are the same thing on both sides
    rec = {k: (None if v == "" else v) for k, v in rec.items()}
    return hashlib.sha1(json.dumps(rec, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def plan(base, notion, repo, prefer=None):
    """Decide each key. Returns (to_repo, to_notion, conflicts, new_base).

    to_repo / to_notion map key -> record, or None for a delete.
    """
    to_repo, to_notion, conflicts, new_base = {}, {}, [], {}
    for key in sorted(set(base) | set(notion) | set(repo)):
        b, n, r = base.get(key), notion.get(key), repo.get(key)
        hn, hr = digest(n), digest(r)
        if hn == hr:
            winner = "same"
        elif hn == b:
            winner = "repo"       # only the repo changed (or added / deleted)
        elif hr == b:
            winner = "notion"     # only Notion changed
        else:
            winner = prefer or "conflict"
        if winner == "conflict":
            conflicts.append(key)
            if b is not None:
                new_base[key] = b
            continue
        if winner == "repo" and hn != hr:
            to_notion[key] = r
        elif winner == "notion" and hn != hr:
            to_repo[key] = n
        final = hn if winner in ("same", "notion") else hr
        if final is not None:
            new_base[key] = final
    return to_repo, to_notion, conflicts, new_base


def describe(key, rec):
    return f"  {'delete' if rec is None else 'write '} {key}"


# --------------------------------------------------
# build: scene files -> the game's data/*.json
# --------------------------------------------------

def build(docs, lang):
    """Fill each target data file's text from the scene files.

    The data file is the template: its other fields (source, note,
    titles, names) are kept as they are. A line with no text in `lang`
    falls back to English.
    """
    written = []
    for doc in docs.values():
        target = doc.get("target")
        if not target:
            continue
        path = os.path.join(ROOT, target["file"])
        data = json.load(open(path, encoding="utf-8"))
        groups = {}
        for line in sorted(doc["lines"], key=lambda l: (l.get("set") or 0, l.get("order") or 0)):
            text = line.get(lang) or line.get("en") or ""
            groups.setdefault(line["group"], {}).setdefault(line.get("set") or 0, []).append(text)
        root = data[target["root"]]
        for g, by_set in groups.items():
            if target["shape"] == "lines":
                root[g]["lines"] = by_set[0]
            else:   # "sets": one list of lines per set, set 1 first
                root[g]["sets"] = [by_set[s] for s in sorted(by_set)]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)   # no newline, as before
        written.append(target["file"])
    return written


# --------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("command", choices=["sync", "status", "build"])
    ap.add_argument("--prefer", choices=["notion", "repo"],
                    help="settle conflicts by taking this side")
    ap.add_argument("--lang", default="en", choices=["en", "ko"],
                    help="language written into data/*.json (default en)")
    args = ap.parse_args()

    docs = read_scene_files()
    if args.command == "build":
        for f in build(docs, args.lang):
            print("built", f)
        return

    env = load_env()
    token = env.get("NOTION_TOKEN")
    if not token:
        sys.exit("NOTION_TOKEN is missing. Copy .env.example to .env and fill it in.")
    dbs = {"lines": env.get("NOTION_LINES_DB", DEFAULT_LINES_DB),
           "scenes": env.get("NOTION_SCENES_DB", DEFAULT_SCENES_DB)}
    client = Notion(token)
    base = json.load(open(STATE_FILE)) if os.path.exists(STATE_FILE) else {}
    notion, pages, scene_pages = notion_records(client, dbs["lines"], dbs["scenes"])
    repo = repo_records(docs)
    to_repo, to_notion, conflicts, new_base = plan(base, notion, repo, args.prefer)

    print(f"Notion -> repo: {len(to_repo)}")
    for k, r in to_repo.items():
        print(describe(k, r))
    print(f"repo -> Notion: {len(to_notion)}")
    for k, r in to_notion.items():
        print(describe(k, r))
    if conflicts:
        print(f"conflicts (changed on both sides, left alone): {len(conflicts)}")
        for k in conflicts:
            print("  " + k)
        print("  settle with: --prefer notion  or  --prefer repo")
    if args.command == "status":
        return

    for k, r in to_repo.items():
        apply_to_repo(docs, k, r)
    for doc in docs.values():
        write_scene_file(doc)
    # scenes first so new lines can point at them
    for k in sorted(to_notion, key=lambda k: not k.startswith("scene:")):
        push_one(client, dbs, pages, scene_pages, k, to_notion[k])
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(new_base, f, indent=1, sort_keys=True)
        f.write("\n")
    for f in build(docs, args.lang):
        print("built", f)


if __name__ == "__main__":
    main()
