"""Present named-file TextStats results through the module CLI.

Argument parsing and output belong here; the file adapter owns UTF-8 input
and the counting core owns newline, word and BOM semantics.
"""

import argparse
import json
import sys
from collections.abc import Sequence

from .files import count_file


def main(argv: Sequence[str] | None = None) -> int:
    """Count one named UTF-8 file and write text or JSON success output.

    Args:
        argv: Command-line arguments without the program name. None selects
            process arguments. --keep-bom retains the leading decoded BOM;
            --json selects one object with integer lines and words fields.

    Returns:
        Zero after writing one lines/words record to stdout; one for read or
        UTF-8 decoding failure with a useful stderr diagnostic and no success
        output. Successful calls produce no stderr and never modify input.

    Raises:
        SystemExit: argparse handles help or invalid command-line arguments.

    The file adapter owns its handles. API read/decode exceptions are translated
    here without a traceback. Stdin remains planned for milestone 2.2;
    at this checkpoint '-' is a literal named file.
    """
    parser = argparse.ArgumentParser(
        prog="python -m textstats", description="Count lines and words in one UTF-8 file."
    )
    parser.add_argument("--keep-bom", action="store_true", help="retain the leading UTF-8 BOM")
    parser.add_argument("--json", action="store_true", help="write counts as a JSON object")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 file")
    arguments = parser.parse_args(argv)
    try:
        result = count_file(arguments.input, strip_bom=not arguments.keep_bom)
    except (OSError, UnicodeDecodeError) as error:
        print(f"textstats: {arguments.input}: {error}", file=sys.stderr)
        return 1
    if arguments.json:
        print(json.dumps({"lines": result.lines, "words": result.words}))
    else:
        print(f"lines={result.lines} words={result.words}")
    return 0
