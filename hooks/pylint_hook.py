"""Pylint hook.

Author: Daniel Yazgi
Date: 2024-05-28
This file is note necessay for now but may be latter since we can get leting statistics.
"""

import argparse
import json
import sys


def main():
    """Main hook function."""
    parser = argparse.ArgumentParser(description="Print colored messages.")
    parser.add_argument("--json-file", dest="json_file" ,type=str,
    help="Input Json file if not it reads from stdin")
    args = parser.parse_args()
    if args.json_file:
        with open(args.json_file, "r", encoding="utf8") as file:
            input_data = file.read()
    else:
        # Read JSON content from stdin
        input_data = sys.stdin.read()

    score = 0
    try:
        # Parse JSON content
        data = json.loads(input_data)
        # Pretty print the parsed JSON data
        score = data["statistics"]["score"]
    except json.JSONDecodeError as err:
        print(f"Failed to decode JSON: {err}")
        sys.exit(1)

    if score < 10:
        print(input_data)
        print(f"\033[91mPylint: Total score {score} is less than 10.\033[0m")
        sys.exit(1)
    else:
        print(f"\033[92mPylint: Total score {score}/10.\033[0m")

if __name__ == "__main__":
    main()
