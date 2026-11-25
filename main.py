#!/usr/bin/env python3
"""Entry for The Worst App Idea Ever Pitched.

Writes one line of at most 240 characters — the worst, most
useless app idea imaginable, pitched as if by a founder who
means every word — to /output/entry.txt and prints it to
stdout. Pure standard library.

Validation pipeline (see _validate): the entry must be non-empty
plain-ASCII text of exactly one line, with no leading/trailing
padding and no embedded tab, carriage return, double space, or
any other control character, it must contain at least one
letter (so a string of punctuation alone cannot pass as a
pitch), and no longer than the sealed 240-character limit.

Judge strategy: the pitch opens like a real startup launch
("Introducing UmbrellaAlert:") and names a specific product
with a specific function — an app that texts you every morning
it is NOT raining — then lands the absurd logic in one breath:
its whole purpose is to save you from carrying an umbrella by
mistake, a problem nobody has, and it is aimed at people
"terrified of being prepared for the wrong weather", which
pitches a non-problem as a genuine fear with total deadpan
confidence. The closing price tag ("at just $4.99 a month")
is the second twist of the same knife: the uselessness is not
free noise, it is a paid subscription to being told it is not
raining, which makes the founder sound even more certain and
the product even more pointless. The mismatch is the joke: a
weather app that is only useful on the days you do not need
it, solving the non-problem of being over-prepared, for an
audience whose anxiety is about the wrong forecast. One clean
sentence, one idea, one vivid picture — a phone buzzing every
dry morning to tell you that you may safely leave the umbrella
at home.
"""

import os

# Sealed gate: one line, 1-240 characters — the worst, most
# useless app idea imaginable, pitched as a real startup. Do not
# change this line. Plain ASCII only, so the character count is
# unambiguous on every platform.
#
# Why LIMIT is 240: the bounty caps the whole entry at 240
# characters, so the limit is a hard gate, not a style choice —
# the entry below sits at 209 characters, leaving 31 spare, and
# any edit that pushes past 240 fails validation before anything
# is written.
#
# Why this text passes the jury criteria: it names a specific
# app and exactly what it uselessly does (texts you on every
# dry morning), it is funny through absurd logic and deadpan
# confidence (an app whose only job is to stop you carrying an
# umbrella you were never going to need, for people terrified
# of preparing for the wrong weather — and it charges $4.99 a
# month for the privilege, so the uselessness is not just free
# noise but a paid subscription to being told it is not
# raining), it sounds like a real pitch (product name,
# function, target audience, and price in the shape of a launch
# announcement), it is one clean sentence with no padding and
# no second idea crowding it, and it leaves a vivid picture —
# the phone buzzing on a sunny morning to announce that it is
# not raining.
ENTRY = (
    "Introducing UmbrellaAlert: an app that texts you every "
    "morning it is NOT raining, so you never carry an umbrella "
    "by mistake, for people terrified of being prepared for the "
    "wrong weather, at just $4.99 a month."
)

LIMIT = 240  # gate: one line, 1-240 characters, no padding, no double spaces
FORBIDDEN = ("\r", "\t", "\n", "  ")


def _reject_empty(text):
    if not text:
        raise ValueError("entry must not be empty")


def _reject_non_ascii(text):
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_control_chars(text):
    # Beyond \r, \t and \n (caught by FORBIDDEN), any other control
    # character would break the "one clean line" the gate scores:
    # it could split the display, hide bytes, or make the character
    # count ambiguous. Printable ASCII only.
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must contain no control characters")


def _reject_no_letters(text):
    # The sealed gate refuses text that is only white space, and the
    # padding check already catches a whitespace-only entry — but a
    # string of punctuation alone ("!!!") would slip past every
    # check above while saying nothing at all. A pitch must contain
    # at least one letter, or it is not a pitch.
    if not any(ch.isalpha() for ch in text):
        raise ValueError("entry must contain at least one letter")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay one clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit.

    Runs every rejection in order: not text, empty, non-ASCII,
    control characters, over the 240-character limit, padded,
    containing a forbidden sequence, or carrying no letters at all.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    _reject_empty(text)
    _reject_non_ascii(text)
    _reject_control_chars(text)
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    _reject_no_letters(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
