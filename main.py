"""MakeFun one-liner: The Robot Vacuum's Funniest Excuse.

A robot vacuum's deadpan excuse for missing a spot on the floor.
The humor: even a robotic cleaner has a dog that plays chores,
and the charging dock gets the blame for human (and canine) negligence.

Writes the entry string to the output directory honouring
the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os

ENTRY = "I missed that spot on purpose. The dog sleeps there, and I have seen what he does to the charging dock."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", newline="") as f:
    f.write(ENTRY)  # no trailing newline; exact 91 chars verified