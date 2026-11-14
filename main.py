"""Copy the entry image to the grader's output directory.

The image (entry.png, a JPEG in fact) lives beside this file in the
repository; the grader runs this program twice and both runs must write
the same bytes, so this is a plain byte copy, standard library only.
After copying, the copy is verified byte for byte against the source:
a truncated copy must fail loudly instead of silently producing an
invalid entry.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)

with open(SRC, "rb") as f:
    source = f.read()
with open(DST, "rb") as f:
    copied = f.read()
if copied != source:
    raise SystemExit("entry.png copy differs from source")
