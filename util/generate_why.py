#!/usr/bin/env python3

"""
Compare the current results to the last results gathered from the main branch to
highlight if a PR is making the results better/worse.
Don't exit with error code if all failing tests are in the ignore-intermittent.txt list.
"""

import argparse
import json
import os
import re
import sys

from utils import flatten_test_results, load_ignore_list


def load_existing_annotations(file_path):
    """Load existing annotations and header from why-error.md."""
    annotations = {}
    header_lines = []
    if not os.path.exists(file_path):
        return header_lines, annotations

    annotation_pattern = re.compile(r"^\*\s+([^\s]+)\s*(.*)")

    with open(file_path, "r") as f:
        found_first_annotation = False
        for line in f:
            sline = line.strip()
            match = annotation_pattern.match(sline)
            if match:
                found_first_annotation = True
                test_path, annotation = match.groups()
                # Remove any text between asterisks (e.g., *INTERMITTENT*)
                annotation = re.sub(r'\s*\*[^*]*\*', '', annotation).strip()
                if annotation:
                    annotations[test_path] = annotation
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
        failing_tests[test] = "INTERMITTENT"

    output_file_path = os.path.join(script_dir, "why-error.md")

    header_lines, existing_annotations = load_existing_annotations(output_file_path)

    with open(output_file_path, "w") as f:
        for line in header_lines:
            f.write(line)
        for test_path, status in sorted(failing_tests.items()):
            out = [ test_path ]

            if status == "INTERMITTENT" or status == "ERROR":
                out += [ f"*{status}*" ]

            annotation = existing_annotations.get(test_path, "")
            if annotation:
                out += [ annotation ]

            f.write(f"* {" ".join(out)}\n")

    print(f"Generated {output_file_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
