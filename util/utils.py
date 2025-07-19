import os

def flatten_test_results(results):
    """Convert nested JSON test results to a flat dictionary of test paths to statuses."""
    flattened = {}
    for util, tests in results.items():
        for test_name, status in tests.items():
            # Build the full test path
            test_path = f"tests/{util}/{test_name}"
            # Remove the .log extension
            test_path = test_path.replace(".log", "")
            flattened[test_path] = status
    return flattened

def load_ignore_list(ignore_file):
    """Load list of tests to ignore from file."""
    if not os.path.exists(ignore_file):
        return set()

    with open(ignore_file, "r") as f:
        return {line.strip() for line in f if line.strip() and not line.startswith("#")}
