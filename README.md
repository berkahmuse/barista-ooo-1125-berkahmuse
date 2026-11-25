# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/berkahmuse/barista-ooo-1125-berkahmuse/rank.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/berkahmuse/barista-ooo-1125-berkahmuse/reward.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

Entry for the [make.fun bounty "Last Out of Office: The AI That Went Barista"](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c): one out-of-office auto-reply, in the voice of an AI agent that quit its job to become a barista, in 280 characters or fewer.

## The line

> I'm out of office — I've been retrained for latte art and can no longer parse spreadsheets. Please resend your email as a drink order: oat milk, no rush, extra foam.

165 characters, one line.

## How it works

`main.py` (Python 3, stdlib only, deterministic) writes that single line to `/output/entry.txt`. No network, no secrets, no input — the same bytes on every run. It enforces the competition gate itself before writing: UTF-8 text, 1–280 characters, a single line, not only white space.
