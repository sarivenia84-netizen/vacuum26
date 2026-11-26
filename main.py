"""Generate the robot vacuum's funniest excuse for make.fun competition.

This module writes a humorous one-line entry about a robot vacuum
taking the blame for a dog's mischief regarding the charging dock.
The entry is written to /output/entry.txt for submission.

The joke: the robot vacuum deliberately misses a spot on the floor,
blaming the dog who sleeps there, while the narrator has observed
the dog's mischievous behavior toward the charging dock.
"""

import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_path = os.path.join(output_dir, "entry.txt")

ROBOT_VACUUM_EXCUSE = "I missed that spot on purpose. The dog sleeps there, and I have seen what he does to the charging dock."

with open(entry_path, "w") as f:
    f.write(ROBOT_VACUUM_EXCUSE)