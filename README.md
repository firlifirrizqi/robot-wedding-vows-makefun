[![Make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/firlifirrizqi/robot-wedding-vows-makefun/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/firlifirrizqi/robot-wedding-vows-makefun/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b) of the same name: one line of wedding vows for a robot couple, at most 160 characters, and funny.

## The line

> In sickness and in low battery, I promise to share my last percent of power with you, and never unplug you first.

## How it works

`main.py` writes that single line (113 characters, within the 160-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. After writing, it re-reads the file and verifies the content is byte-identical, 1–160 characters, and not only whitespace.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
