#!/usr/bin/env python3

"""
Compare the current results to the last results gathered from the main branch to
highlight if a PR is making the results better/worse.
Don't exit with error code if all failing tests are in the ignore-intermittent.txt list.
"""

import argparse
import json
import os
import sys

from utils import flatten_test_results, load_ignore_list

def load_existing_annotations(file_path):
    """Load existing annotations and header from why-error.md."""
    annotations = {}
    header_lines = []
    if not os.path.exists(file_path):
        return header_lines, annotations

    with open(file_path, "r") as f:
        found_first_annotation = False
        for line in f:
            sline = line.strip()
            if sline.startswith("* "):
                found_first_annotation = True
                parts = sline[2:].split(" ", 1)
                test_path = parts[0]
                if len(parts) > 1:
                    annotations[test_path] = parts[1]
            elif not found_first_annotation:
                header_lines.append(line)
    return header_lines, annotations

def main():
    script_dir = os.path.dirname(__file__)

    parser = argparse.ArgumentParser(
        description="Re-generate why-error.md and why-skip.md"
    )
    parser.add_argument(
        "--results-json",
        default=os.path.join(script_dir, "aggregated-result.json"),
        help="Path to a run JSON aggregate_results.json",
    )
    parser.add_argument(
        "--ignore-file",
        default=os.path.join(script_dir, "..", ".github", "workflows", "ignore-intermittent.txt"),
        help="Path to file with tests to ignore (for intermittent issues)",
    )

    args = parser.parse_args()

    # Load test results
    try:
        with open(args.results_json, "r") as f:
            results = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        sys.stderr.write(f"Error loading current results: {e}\n")
        return 1

    # Load ignore list (required)
    if not os.path.exists(args.ignore_file):
        sys.stderr.write(f"Error: Ignore file {args.ignore_file} does not exist\n")
        return 1

    ignore_list = load_ignore_list(args.ignore_file)

    print(f"Loaded {len(ignore_list)} tests to ignore from {args.ignore_file}")

    flat = flatten_test_results(results)

    failing_tests = {test: status for test, status in flat.items() if status in ("FAIL", "ERROR")}

    for test in ignore_list:
        failing_tests[test] = "IGNORED"

    output_file_path = os.path.join(script_dir, "why-error.md")

    header_lines, existing_annotations = load_existing_annotations(output_file_path)

    with open(output_file_path, "w") as f:
        for line in header_lines:
            f.write(line)
        for test_path, status in sorted(failing_tests.items()):
            annotation = existing_annotations.get(test_path, "")
            if annotation:
                f.write(f"* {test_path} {annotation}\n")
            else:
                f.write(f"* {test_path}\n")

    print(f"Generated {output_file_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
