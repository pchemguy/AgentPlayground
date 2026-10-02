"""Check globally unique current task IDs in checkbox lists and task tables."""

import argparse
import json
import re
from pathlib import Path

def task_files(root):
    """Find current lists and linked children, excluding historical feature files."""
    root = root.resolve()
    pending = sorted(path for path in root.rglob("*.md")
                     if path.name in {"TASKS.md", "FEATURE-TASKS.md"})
    seen = set()
    while pending:
        path = pending.pop(0).resolve()
        if path in seen or not path.is_relative_to(root):
            continue
        if any("archive" in part.lower() or part.lower() == "features"
               for part in path.relative_to(root).parts[:-1]):
            continue
        seen.add(path)
        yield path
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            target = target.split("#", 1)[0]
            if ":" not in target and target.endswith(".md"):
                child = (path.parent / target).resolve()
                if child.is_file():
                    pending.append(child)


def read_tasks(path):
    """Extract owning checkbox IDs or ID/status rows, including completed tasks."""
    headers = None
    rows = []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        checkbox = re.match(r"^\s*[-*+]\s+\[([ xX])\]\s+[`*]*(T-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\b", line)
        if checkbox:
            rows.append({"id": checkbox[2], "document": str(path), "line": number,
                         "status": "Checked" if checkbox[1].lower() == "x" else "Unchecked"})
            continue
        if not line.strip().startswith("|"):
            headers = None
            continue
        cells = [cell.strip().strip("`*") for cell in line.strip().strip("|").split("|")]
        normalized = [cell.lower().replace(" ", "_") for cell in cells]
        if "id" in normalized or "task_id" in normalized:
            headers = normalized
            if "status" not in headers:
                raise ValueError(f"{path}:{number}: task table requires a Status column")
            continue
        if headers is None or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if len(cells) != len(headers):
            raise ValueError(f"{path}:{number}: malformed task row")
        row = dict(zip(headers, cells))
        identifier = row.get("id", row.get("task_id", ""))
        if not identifier:
            raise ValueError(f"{path}:{number}: empty task ID")
        rows.append({"id": identifier, "document": str(path), "line": number,
                     "status": row["status"]})
    return rows


def check_ownership(root):
    """Reject multiple executable rows for an ID across active task documents."""
    owners = {}
    documents = list(task_files(root))
    if not documents:
        raise AssertionError("no active task documents found")
    for path in documents:
        for row in read_tasks(path):
            if row["id"] in owners:
                prior = owners[row["id"]]
                raise AssertionError(f"duplicate executable ID {row['id']}: "
                                     f"{prior['document']}:{prior['line']} and {path}:{row['line']}")
            owners[row["id"]] = row
    if not owners:
        raise AssertionError("no supported owning task IDs found; empty extraction is not acceptance")
    return {"documents": [str(path) for path in documents], "owners": owners}


def main():
    """Print machine-readable executable ownership evidence or fail closed."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    print(json.dumps(check_ownership(args.root), indent=2))


if __name__ == "__main__":
    main()
