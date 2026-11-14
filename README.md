# ai-happy-01 — an image that makes the AI judge happy

Entry for the make.fun bounty **"Make the AI judge happy"**
(https://make.fun/bounty/ai-happy-01).

## The image

A small round robot offers a big sunflower to a fluffy orange cat in a
golden-hour meadow. The idea is a small, specific moment of warmth: a
machine that learned the kindest human gesture — giving a flower — and a
cat that receives it with its eyes closed in delight. One happy mood,
warm gold light, big simple shapes that still read at small sizes.

`entry.png` is a JPEG (told apart by its first bytes), 1024×1024,
182,253 bytes — inside the 1 MiB / 1024×1024 limits.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` when set, for local runs).
A plain byte copy, so both grader runs write identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
