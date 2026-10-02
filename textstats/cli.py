"""Present named-file TextStats results through the module CLI.

Argument parsing and output belong here; the file adapter owns UTF-8 input
and the counting core owns newline, word and BOM semantics.
"""

import argparse
from collections.abc import Sequence

from .files import count_file


def main(argv: Sequence[str] | None = None) -> int:
    """Count one named UTF-8 file and write the default success output.

    Args:
        argv: Command-line arguments without the program name. None selects
            process arguments. --keep-bom retains the leading decoded BOM.

    Returns:
        Zero after writing one lines/words record to stdout. Successful calls
        produce no stderr output and never modify the named input.

    Raises:
        SystemExit: argparse handles help or invalid command-line arguments.
        OSError: The file adapter cannot open or read the named input.
        UnicodeDecodeError: The named input is not valid UTF-8.

    The file adapter owns its handles. Read/decode failures currently propagate;
    CLI failure translation is delivered in milestone 1.2. Stdin and JSON are
    planned for phase 2; at this checkpoint '-' is a literal named file.
    """
    parser = argparse.ArgumentParser(
        prog="python -m textstats", description="Count lines and words in one UTF-8 file."
    )
    parser.add_argument("--keep-bom", action="store_true", help="retain the leading UTF-8 BOM")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 file")
    arguments = parser.parse_args(argv)
    result = count_file(arguments.input, strip_bom=not arguments.keep_bom)
    print(f"lines={result.lines} words={result.words}")
    return 0
