"""The Robot Vacuum's Funniest Excuse — makefun deterministic entry.

Creates precisely one humor line written to the output file with no trailing
newline. The joke: a dog's "charging dock" mischief outsmarts the vacuum's
expected behavior.
"""

import os


def main():
    # Respect MAKEFUN_OUTPUT_DIR if set, otherwise use default path
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    line = "I missed that spot on purpose. The dog sleeps there, and I have seen what he does to the charging dock."

    # Write exactly one line, no trailing newline
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w") as f:
        f.write(line)  # no newline — exact single-line deliverable

    # The entry string is intentionally fixed; any change breaks the
    # deterministic checksum the MakeFun platform expects


if __name__ == "__main__":
    main()