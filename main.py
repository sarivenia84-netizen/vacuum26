"""MakeFun entry: The Robot Vacuum's Funniest Excuse."""

import os


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    line = "I missed that spot on purpose. The dog sleeps there, and I have seen what he does to the charging dock."
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()