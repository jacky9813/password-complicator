import argparse
import getpass

from .password_complicator import HASH_OPTIONS, DEFAULT_HASH_FUNCTION
from .password_complicator import ENCODING_OPTIONS, DEFAULT_ENCODING_OPTION
from .password_complicator import DEFAULT_LENGTH
from . import obfuscate, __version__

def parse_command_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Making password more complicated with hashing and encoding."
    )
    parser.add_argument(
        "--hash",
        "-d",
        choices=HASH_OPTIONS.keys(),
        default=DEFAULT_HASH_FUNCTION,
        help=f"The hash algorithm to be used. (Default: {DEFAULT_HASH_FUNCTION})"
    )
    parser.add_argument(
        "--encoding",
        "-e",
        choices=ENCODING_OPTIONS.keys(),
        default=DEFAULT_ENCODING_OPTION,
        help=f"The encoding for the result of the hash digest. (Default: {DEFAULT_ENCODING_OPTION})"
    )
    parser.add_argument(
        "--length",
        "-l",
        type=int,
        default=DEFAULT_LENGTH,
        help=f"The maximum length of the output string. (Default: {DEFAULT_LENGTH})"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__
    )
    return parser.parse_args()


def main():
    args = parse_command_args()
    raw_password = getpass.getpass()
    print(obfuscate(raw_password, args.hash, args.encoding, args.length))

if __name__ == "__main__":
    main()