"""
Author: Daniel Yazgi
Date: 2024-05-28
"""

import sys
import json
import argparse

def main():

    parser = argparse.ArgumentParser(description="Print colored messages.")
    parser.add_argument('--json_file', dest="json_file" ,type=str, help='Input Json file if not it reads from stdin')
    args = parser.parse_args()
    if args.json_file:
        with open(args.json_file, 'r', encoding="utf8") as file:
            input_data = json.load(file)
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

if __name__ == "__main__":
    main()
