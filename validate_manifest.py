#!/usr/bin/env python3
"""Validate a Component Manifest against its snapshot (schema v2.1).

Usage: python validate_manifest.py snapshot.txt manifest.md

Checks: document shape, headings, one table per section with exact columns,
locator syntax and truth (I3 locators), file coverage (I1), line coverage (I2),
Section 2 Lines / Mapped to values, Section 7 run rules, row ordering, and that
code-span values appear verbatim in the cited lines.

Not checked (needs judgment): I4 no inference, whether every declaration was
routed to Section 3, and the doc-code-mismatch comparison.
"""
import re
import sys

HEADINGS = [
    "1. Repository Record", "2. Source Coverage", "3. Component Manifest",
    "4. Dependency Manifest", "5. Route Manifest", "6. Configuration Manifest",
    "7. Unmapped Source Items", "8. Translation Exceptions",
]
COLUMNS = {
    1: ["Field", "Value", "Source"],
    2: ["Path", "Lines", "Mapped to", "Source"],
    3: ["ID", "Kind", "Name", "Definition", "Stated role", "Evidence"],
    4: ["Name", "Version", "Group", "Source"],
    5: ["Route", "Declaration", "Evidence"],
    6: ["Key", "Value", "Evidence"],
    7: ["Path", "Item", "Evidence"],
    8: ["#", "Type", "Exception", "Evidence"],
}
LOC_COL = {1: "Source", 2: "Source", 3: "Evidence", 4: "Source",
           5: "Evidence", 6: "Evidence", 7: "Evidence", 8: "Evidence"}
# columns whose code spans must appear verbatim in the cited lines
VERBATIM_COLS = {1: ["Value"], 3: ["Kind", "Name", "Definition"], 4: ["Name", "Version"],
                 5: ["Route", "Declaration"], 6: ["Value"], 7: ["Item"], 8: ["Exception"]}
GROUPS = {"dependencies", "devDependencies", "peerDependencies", "optionalDependencies",
          "import", "import-local", "readme-mention"}
EXC_TYPES = {"missing-referenced-file", "doc-code-mismatch", "unreadable-content",
             "header-missing", "unnumbered-source"}
NIS = "not in source"
NONE = "none found in source"

errors = []


def err(msg):
    errors.append(msg)


# ---------- snapshot ----------
def parse_snapshot(text):
    lines = text.splitlines()
    header = {}
    tree = []
    files = {}
    i = 0
    n = len(lines)
    while i < n and not lines[i].startswith("--- BEGIN") and lines[i].strip() != "FILE TREE":
        m = re.match(r"^(REPOSITORY IDENTIFIER|SOURCE SNAPSHOT IDENTIFIER)", lines[i].strip())
        if m:
            key = ("repository-identifier" if m.group(1).startswith("REPOSITORY")
                   else "source-snapshot-identifier")
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and lines[j].strip() not in ("FILE TREE",) and not lines[j].startswith("SOURCE"):
                header[key] = lines[j].strip()
            i = j
        i += 1
    while i < n and lines[i].strip() != "FILE TREE":
        i += 1
    i += 1
    while i < n and lines[i].strip() and not lines[i].startswith("--- "):
        tree.append(lines[i].strip())
        i += 1
    cur = None
    for ln in lines[i:]:
        m = re.match(r"^--- (.+?) ---$", ln)
        if m and not ln.startswith("--- BEGIN") and not ln.startswith("--- END"):
            cur = m.group(1)
            files[cur] = {}
            continue
        if ln.startswith("--- END"):
            cur = None
            continue
        if cur is not None:
            m = re.match(r"^(\d+):(?: ?(.*))?$", ln)
            if m:
                files[cur][int(m.group(1))] = m.group(2) or ""
    return header, tree, files


def is_exempt(text):
    t = text.strip()
    if not t:
        return True
    if t.startswith("```"):
        return True
    return re.fullmatch(r"[\[\]{}(),;\s]+", t) is not None


# ---------- manifest ----------
def split_cells(line):
    parts = re.split(r"(?<!\\)\|", line.strip())
    if parts and parts[0] == "":
        parts = parts[1:]
    if parts and parts[-1] == "":
        parts = parts[:-1]
    return [c.strip() for c in parts]


def parse_manifest(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "# Component Manifest":
        err("First line must be exactly '# Component Manifest'")
    sections = {}
    cur = None
    order = []
    for idx, ln in enumerate(lines[1:], start=2):
        m = re.match(r"^## (\d)\. (.+)$", ln)
        if m:
            cur = int(m.group(1))
            order.append((cur, f"{m.group(1)}. {m.group(2)}"))
            sections[cur] = []
            continue
        if cur is None:
            if ln.strip():
                err(f"Line {idx}: text before Section 1: {ln.strip()[:50]}")
            continue
        sections[cur].append(ln)
    if [h for _, h in order] != HEADINGS:
        err(f"Section headings wrong or out of order: {[h for _, h in order]}")
    parsed = {}
    for num, body in sections.items():
        body = [b for b in body if b.strip()]
        if body == [NONE]:
            if num in (1, 2):
                err(f"Section {num} may not be empty")
            parsed[num] = []
            continue
        if not body or not all(b.lstrip().startswith("|") for b in body):
            err(f"Section {num}: must be one table or the line '{NONE}'")
            parsed[num] = []
            continue
        header = split_cells(body[0])
        if header != COLUMNS[num]:
            err(f"Section {num}: columns {header} != {COLUMNS[num]}")
        if len(body) < 3 or not re.fullmatch(r"[|\s:-]+", body[1]):
            err(f"Section {num}: missing header separator row")
            parsed[num] = []
            continue
        rows = []
        for r in body[2:]:
            cells = split_cells(r)
            if len(cells) != len(COLUMNS[num]):
                err(f"Section {num}: row has {len(cells)} cells, expected "
                    f"{len(COLUMNS[num])}: {r[:60]}")
                continue
            rows.append(dict(zip(COLUMNS[num], cells)))
        parsed[num] = rows
    return parsed


LOC_TOKEN = re.compile(r"\[[^\]]*\]")
LOC_PATH = re.compile(r"^\[([^\]:\s]+):(\d+)-(\d+)\]$")
LOC_HDR = re.compile(r"^\[header:(repository-identifier|source-snapshot-identifier)\]$")


def parse_locators(cell, where):
    """Return list of ('path', p, a, b) / ('header', key) / ('tree',). None if NIS."""
    if cell == NIS:
        return None
    toks = LOC_TOKEN.findall(cell)
    if not toks or " ".join(toks) != cell:
        err(f"{where}: cell must be only locators separated by single spaces or "
            f"'{NIS}': {cell[:60]}")
        return []
    out = []
    for t in toks:
        m = LOC_PATH.match(t)
        if m:
            a, b = int(m.group(2)), int(m.group(3))
            out.append(("path", m.group(1), a, b))
        elif LOC_HDR.match(t):
            out.append(("header", LOC_HDR.match(t).group(1)))
        elif t == "[tree]":
            out.append(("tree",))
        else:
            err(f"{where}: invalid locator {t}")
    return out


def code_spans(cell):
    return [s.replace("\\|", "|") for s in re.findall(r"`([^`]+)`", cell)]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def main(snap_path, man_path):
    header, tree, files = parse_snapshot(open(snap_path).read())
    parsed = parse_manifest(open(man_path).read())

    covered = {p: set() for p in files}           # lines cited by sections 3-6
    covered7 = {p: set() for p in files}          # lines cited by section 7
    cites_by_path = {p: set() for p in tree}       # sections 3-7 citing each path
    row_order = {}

    for num in range(1, 9):
        rows = parsed.get(num, [])
        col = LOC_COL[num]
        last_key = None
        for ri, row in enumerate(rows, start=1):
            where = f"Section {num} row {ri}"
            locs = parse_locators(row[col], where)
            if locs is None:
                allowed = (num == 1 and row["Value"] == NIS) or \
                          (num == 8 and row["Type"] == "header-missing")
                if not allowed:
                    err(f"{where}: '{NIS}' as {col} is only allowed for a missing header "
                        f"value or a header-missing exception")
                locs = []
            elif not locs:
                err(f"{where}: no locator")
            texts = []
            for loc in locs:
                if loc[0] == "path":
                    _, p, a, b = loc
                    if p not in files:
                        err(f"{where}: locator path '{p}' has no supplied content")
                        continue
                    nl = max(files[p]) if files[p] else 0
                    if not (1 <= a <= b <= nl):
                        err(f"{where}: locator [{p}:{a}-{b}] outside 1-{nl}")
                        continue
                    texts.extend(files[p].get(k, "") for k in range(a, b + 1))
                    if 3 <= num <= 6:
                        covered[p].update(range(a, b + 1))
                    if num == 7:
                        covered7[p].update(range(a, b + 1))
                    if 3 <= num <= 7:
                        cites_by_path.setdefault(p, set()).add(num)
                elif loc[0] == "header":
                    v = header.get(loc[1])
                    if v is None:
                        err(f"{where}: header value {loc[1]} not supplied")
                    else:
                        texts.append(v)
                else:
                    texts.extend(tree)
            # verbatim check
            blob = norm("\n".join(t.strip() for t in texts))
            for colname in VERBATIM_COLS.get(num, []):
                for span in code_spans(row.get(colname, "")):
                    if norm(span) not in blob:
                        err(f"{where}: `{span}` ({colname}) not found verbatim in cited lines")
            # ordering (sections 3-7): tree order, then start line
            first = next((l for l in locs if l[0] == "path"), None)
            if 3 <= num <= 7 and first and first[1] in tree:
                key = (tree.index(first[1]), first[2])
                if last_key and key < last_key:
                    err(f"{where}: rows out of order (tree order, then line)")
                last_key = key

    # Section 1
    s1 = parsed.get(1, [])
    expect = [("repository_identifier", "repository-identifier"),
              ("source_snapshot_identifier", "source-snapshot-identifier")]
    if [r["Field"].strip("`") for r in s1] != [e[0] for e in expect]:
        err("Section 1 must have exactly repository_identifier then source_snapshot_identifier")

    # Section 3 IDs
    for i, row in enumerate(parsed.get(3, []), start=1):
        if row["ID"] != f"component-{i:03d}":
            err(f"Section 3 row {i}: ID should be component-{i:03d}, got {row['ID']}")

    # Section 4 groups, Section 8 types
    for i, row in enumerate(parsed.get(4, []), start=1):
        if row["Group"] not in GROUPS:
            err(f"Section 4 row {i}: invalid Group '{row['Group']}'")
    for i, row in enumerate(parsed.get(8, []), start=1):
        if row["Type"] not in EXC_TYPES:
            err(f"Section 8 row {i}: invalid Type '{row['Type']}'")
        if row["#"] != str(i):
            err(f"Section 8 row {i}: # should be {i}")

    # I1 + Section 2 values
    s2 = parsed.get(2, [])
    paths = [r["Path"].strip("`") for r in s2]
    if sorted(paths) != sorted(tree) or len(set(paths)) != len(paths):
        err(f"I1: Section 2 paths {paths} != FILE TREE {tree} (each exactly once)")
    for row in s2:
        p = row["Path"].strip("`")
        if p not in tree:
            continue
        if p in files:
            want_lines = str(max(files[p]) if files[p] else 0)
        else:
            want_lines = "not supplied"
        if row["Lines"] != want_lines:
            err(f"Section 2 {p}: Lines {row['Lines']} != {want_lines}")
        want_map = ", ".join(str(x) for x in sorted(cites_by_path.get(p, set()))) or "none"
        if row["Mapped to"] != want_map:
            err(f"Section 2 {p}: Mapped to '{row['Mapped to']}' != '{want_map}'")

    # I2 + Section 7 run rules
    for p, lines in files.items():
        is_md = p.lower().endswith(".md")
        fence = False
        fenced = set()
        for k in sorted(lines):
            if is_md and lines[k].strip().startswith("```"):
                fence = not fence
                continue
            if fence:
                fenced.add(k)

        def uncited(k):
            return (k in lines and not is_exempt(lines[k]) and k not in covered[p])

        for k in sorted(lines):
            if uncited(k) and k not in covered7[p]:
                err(f"I2: {p}:{k} not cited by any row: {lines[k].strip()[:50]}")
        for row in parsed.get(7, []):
            if row["Path"].strip("`") != p:
                continue
            locs = parse_locators(row["Evidence"], "Section 7")
            for loc in locs or []:
                if loc[0] != "path" or loc[1] != p:
                    continue
                _, _, a, b = loc
                for k in range(a, b + 1):
                    if k not in lines:
                        continue
                    if not uncited(k):
                        err(f"Section 7 [{p}:{a}-{b}]: line {k} is blank, exempt, or "
                            f"already cited elsewhere; runs must be split there")
                    if is_md and k != a and lines[k].lstrip().startswith("#") and k not in fenced:
                        err(f"Section 7 [{p}:{a}-{b}]: heading at line {k} must start a new run")
                if uncited(a - 1) or uncited(b + 1):
                    err(f"Section 7 [{p}:{a}-{b}]: run is not maximal (adjacent uncited line)")
                if a in lines and norm(lines[a]) != norm(" ".join(code_spans(row["Item"]))):
                    err(f"Section 7 [{p}:{a}-{b}]: Item is not the first line of the run")

    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS: all checks succeeded")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
