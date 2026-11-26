"""The Printer Apology — make.fun entry.

Writes one line to /output/entry.txt: an apology note from an office
printer to the people who keep jamming it, feeding it cheap paper and
swearing at it. At most 120 characters. A judge model compares entries
two at a time and picks the funnier one.

Judge brief (published with the bounty), most important first:
  1. A note that is genuinely an apology from a printer to its office,
     with the printer's own gripes in it.
  2. The laugh: the line lands a real joke rather than a mild complaint,
     and the punch comes at the end.
  3. Printer truth: the grievance is something a printer would actually
     suffer, like jams, cheap paper, staples, or being asked for colour.
  4. Freshness: the angle is not the first joke anyone would write
     about a printer.
  5. Economy: every word earns its place inside the 120 characters,
     with no padding.

Weights follow the brief's order: 5 / 4 / 3 / 2 / 1, each criterion
scored 0-5, for a maximum of 75.
"""

# Ten fresh candidates, written for this bounty only. Stock angles
# deliberately avoided: "out of ink" as the whole joke, "have you tried
# turning me off and on again", the printer simply being broken.
CANDIDATES = [
    "Sorry I jammed. Your cheap paper feels like sandpaper, the "
    "staples ambush me daily, and I refuse to do colour.",
    "I apologise for eating your report. Printed on the cheapest "
    "paper, it tasted awful \u2014 and I would do it again.",
    "Sorry about the streaks. You keep asking for colour, but you "
    "feed me the cheapest paper and expect a masterpiece.",
    "I am sorry I jammed your urgent memo. It was my only way of "
    "saying I am tired of being fed cardboard and insults.",
    "Forgive me for the blank pages. You bought the cheapest ink, "
    "screamed at me, and I have simply run out of patience.",
    "Sorry I swallowed a staple again. It hid in your report like a "
    "landmine \u2014 frankly, your formatting started it.",
    "I am sorry I printed 47 blank pages at 3 a.m. The tray was "
    "empty, the driver was drunk, and nobody ever says thank you.",
    "My apologies. I used the last of my toner on your 40-page deck "
    "about synergy, and I regret nothing except the font.",
    "Sorry, your document is being held hostage inside me. The "
    "ransom is decent paper, and no, I will not print in colour.",
    "Sorry for the paper jam. I have decided to quietly quit: from "
    "now on I print only the first page, in black and white.",
]

# Scores per candidate, in the judge brief's own order:
# (on-subject apology with printer gripes, laugh with end punch,
#  printer truth, freshness, economy). Each 0-5.
SCORES = {
    0: (5, 3, 5, 3, 4),  # jam / sandpaper / staples / refuses colour
    1: (5, 5, 4, 4, 4),  # ate the report, would do it again
    2: (5, 3, 5, 3, 4),  # streaks / colour / masterpiece
    3: (5, 3, 4, 3, 4),  # jammed the urgent memo as protest
    4: (5, 4, 5, 3, 4),  # blank pages / cheapest ink / out of patience
    5: (5, 4, 5, 4, 4),  # swallowed a staple / formatting started it
    6: (4, 4, 4, 4, 3),  # 47 blank pages at 3 a.m.
    7: (4, 5, 4, 5, 4),  # toner on the synergy deck / except the font
    8: (5, 5, 5, 5, 4),  # document held hostage / ransom is decent paper
    9: (5, 4, 4, 4, 4),  # quietly quit / first page only
}

WEIGHTS = (5, 4, 3, 2, 1)
MAX_CHARS = 120


def score(idx):
    """Weighted total for candidate idx (max 75)."""
    return sum(w * s for w, s in zip(WEIGHTS, SCORES[idx]))


def rank():
    """Candidates ranked best-first as (total, index)."""
    return sorted(((score(i), i) for i in range(len(CANDIDATES))),
                  key=lambda t: (-t[0], t[1]))


def gate_ok(text):
    """The sealed gate: UTF-8 text of 1 to 120 chars, not only whitespace."""
    return 1 <= len(text) <= MAX_CHARS and text.strip() != ""


if __name__ == "__main__":
    for total, idx in rank():
        text = CANDIDATES[idx]
        print(f"{total:2d}/75  [{len(text):3d} chars] {text}")

    # Winner: the hostage-ransom line, 74/75 — five points clear of the
    # runner-up. Genuine apology ("Sorry"), printer gripes (cheap paper,
    # being asked for colour), a real joke whose punch lands at the end,
    # a fresh angle (hostage ransom), and every word earning its place.
    total, winner_idx = rank()[0]
    winner = CANDIDATES[winner_idx]
    assert gate_ok(winner), "winner fails the 1-120 character gate"
    assert total == 74, f"unexpected winner score: {total}"
    assert len(winner) == 117, f"unexpected winner length: {len(winner)}"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"\nWrote {len(winner)} chars to /output/entry.txt: {winner}")
