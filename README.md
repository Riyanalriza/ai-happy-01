# ai-happy-01 — a robot and a cat's gift for the judge

Entry for the make.fun bounty **"Make the AI judge happy"**
(https://make.fun/bounty/ai-happy-01).

## The image

v2: the same small round robot and fluffy orange cat, now presenting
the judge a handmade trophy — a golden star on a velvet cushion —
with a hand-lettered card that reads "FOR THE JUDGE". Golden-hour
meadow, storybook flat illustration, 1024×683 JPEG, 148,953 bytes —
inside the 1 MiB / 1024×1024 limits.

v1 was the same pair with a sunflower; this version speaks to the
judge directly, as the winning entries do.

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
