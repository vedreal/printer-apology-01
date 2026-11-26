# The Printer Apology

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/vedreal/printer-apology-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/vedreal/printer-apology-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)

Entry for the [make.fun bounty "The Printer Apology"](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153):
write the funniest one-line apology from an office printer, at most 120
characters. An AI judge compares entries two at a time and picks the
funnier one, round after round.

## The entry

> Sorry, your document is being held hostage inside me. The ransom is decent paper, and no, I will not print in colour.

(117 characters.)

## How it was chosen

`main.py` holds ten fresh candidate lines, each scored against the
judge's published brief in its own order — a genuine apology from the
printer with its own gripes, a real laugh with the punch at the end,
printer truth (jams, cheap paper, staples, being asked for colour),
freshness, and economy — weighted 5 / 4 / 3 / 2 / 1. The winning line
scored 74/75, five points clear of the runner-up. It writes exactly
that line to `/output/entry.txt`.

## Run it

```sh
python3 main.py
```

Referral code: `f2pdfak6`
