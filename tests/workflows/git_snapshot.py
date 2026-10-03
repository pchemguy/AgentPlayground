"""Capture read-only Git evidence without exposing remote URLs or credentials."""

import argparse
import json
import subprocess
from pathlib import Path


def git(repo, *args):
    """Run a literal read-only Git command and return its standard output."""
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def capture(repo, remote="origin"):
    """Capture HEAD ancestry, worktree state, changed paths and remote refs."""
    head = git(repo, "rev-parse", "HEAD")
    parents = git(repo, "rev-list", "--parents", "-n", "1", head).split()[1:]
    remote_refs = {}
    for line in git(repo, "ls-remote", "--heads", remote).splitlines():
        oid, ref = line.split("\t")
        remote_refs[ref] = oid
    return {
        "schema_version": 1,
        "branch": git(repo, "branch", "--show-current"), "head": head,
        "parents": parents,
        "status": git(repo, "status", "--porcelain=v1", "--untracked-files=all").splitlines(),
        "remote": remote, "remote_heads": remote_refs,
        "changed_paths": git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r",
                             parents[0], head).splitlines() if parents else [],
    }


def check_boundary(snapshot, branch, first_parent, second_parent, allowed_paths,
                   require_clean=True, require_remote=False):
    """Reject wrong branch, ancestry, scope, dirty state or unpublished HEAD."""
    errors = []
    if snapshot["branch"] != branch:
        errors.append("branch differs from the literal expected branch")
    if snapshot["parents"] != [first_parent, second_parent]:
        errors.append("boundary must have exactly two ordered expected parents")
    if require_clean and snapshot["status"]:
        errors.append("worktree is dirty")
    for path in snapshot["changed_paths"]:
        if not any(path == root or path.startswith(root.rstrip("/") + "/")
                   for root in allowed_paths):
            errors.append(f"changed path outside allowed scope: {path}")
    if require_remote and snapshot["remote_heads"].get("refs/heads/" + branch) != snapshot["head"]:
        errors.append("remote branch does not equal captured HEAD")
    if errors:
        raise AssertionError("; ".join(errors))


def main():
    """Write a snapshot or check one against assessor supplied literal values."""
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    take = commands.add_parser("capture")
    take.add_argument("repo", type=Path)
    take.add_argument("output", type=Path)
    take.add_argument("--remote", default="origin")
    check = commands.add_parser("check")
    check.add_argument("snapshot", type=Path)
    check.add_argument("--branch", required=True)
    check.add_argument("--first-parent", required=True)
    check.add_argument("--second-parent", required=True)
    check.add_argument("--allow", action="append", required=True)
    check.add_argument("--require-remote", action="store_true")
    args = parser.parse_args()
    if args.command == "capture":
        args.output.write_text(json.dumps(capture(args.repo, args.remote), indent=2) + "\n")
    else:
        check_boundary(json.loads(args.snapshot.read_text()), args.branch,
                       args.first_parent, args.second_parent, args.allow,
                       require_remote=args.require_remote)


if __name__ == "__main__":
    main()
