## Usage: python script.py /path/to/folder _c_c

import os
import argparse


def rename_remove(directory: str, part: str) -> None:
    for name in os.listdir(directory):
        if part in name:
            new_name = name.replace(part, "")
            src = os.path.join(directory, name)
            dst = os.path.join(directory, new_name)

            if src != dst:
                os.rename(src, dst)


def rename_remove_suffix(directory: str, suffix: str) -> None:
    for name in os.listdir(directory):
        if name.endswith(suffix):
            new_name = name[: -len(suffix)]
            src = os.path.join(directory, name)
            dst = os.path.join(directory, new_name)

            if src != dst:
                os.rename(src, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch rename files by removing a substring or suffix.")
    
    parser.add_argument("directory", help="Target directory")
    parser.add_argument("pattern", help="Substring or suffix to remove")
    parser.add_argument(
        "--suffix",
        action="store_true",
        help="Interpret pattern as suffix (removes only if at the end)",
    )

    args = parser.parse_args()

    if args.suffix:
        rename_remove_suffix(args.directory, args.pattern)
    else:
        rename_remove(args.directory, args.pattern)