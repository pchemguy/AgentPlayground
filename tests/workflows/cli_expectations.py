"""Record subprocess results and compare externally authored literal expectations."""

import argparse
import json
import subprocess
from pathlib import Path


def run_expectation(expectation, cwd):
    """Compare exact exit status and output, with no product imports or inference."""
    command = expectation["argv"]
    if not command or not all(isinstance(part, str) for part in command):
        raise ValueError("argv must be a nonempty array of literal strings")
    result = subprocess.run(command, cwd=cwd, input=expectation.get("stdin", ""),
                            capture_output=True, text=True,
                            timeout=expectation.get("timeout_seconds", 30), shell=False)
    actual = {"argv": command, "returncode": result.returncode,
              "stdout": result.stdout, "stderr": result.stderr}
    actual["mismatches"] = [key for key in ("returncode", "stdout", "stderr")
                            if actual[key] != expectation[key]]
    return actual


def main():
    """Persist actual evidence before returning failure for any literal mismatch."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expectation", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--cwd", type=Path, required=True)
    args = parser.parse_args()
    actual = run_expectation(json.loads(args.expectation.read_text()), args.cwd)
    args.output.write_text(json.dumps(actual, indent=2) + "\n")
    raise SystemExit(bool(actual["mismatches"]))


if __name__ == "__main__":
    main()
