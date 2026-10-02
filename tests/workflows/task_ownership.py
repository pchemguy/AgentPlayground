"""Check unique executable task IDs from explicit Markdown task tables."""

import argparse
import json
import re
from pathlib import Path

TERMINAL = {"done", "complete", "completed", "cancelled", "canceled", "superseded", "archived"}


def task_files(root):
    """Find governing task documents while excluding archive directory components."""
    for path in sorted(root.rglob("*.md")):
        if path.name not in {"TASKS.md", "FEATURE-TASKS.md"}:
            continue
        if any("archive" in part.lower() for part in path.relative_to(root).parts[:-1]):
            continue
        yield path


def read_tasks(path):
    """Extract ID/status table rows; reject ambiguous executable table schemas."""
    headers = None
    rows = []
    saw_table = False
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if not line.strip().startswith("|"):
            headers = None
            continue
        cells = [cell.strip().strip("`*") for cell in line.strip().strip("|").split("|")]
        normalized = [cell.lower().replace(" ", "_") for cell in cells]
        if "id" in normalized or "task_id" in normalized:
            headers = normalized
            saw_table = True
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
        if row["status"].lower() not in TERMINAL:
            rows.append({"id": identifier, "document": str(path), "line": number,
                         "status": row["status"]})
    if not saw_table:
        raise ValueError(f"{path}: no supported ID/Status task table found")
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
    return {"documents": [str(path) for path in documents], "owners": owners}


def main():
    """Print machine-readable executable ownership evidence or fail closed."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    print(json.dumps(check_ownership(args.root), indent=2))


if __name__ == "__main__":
    main()
