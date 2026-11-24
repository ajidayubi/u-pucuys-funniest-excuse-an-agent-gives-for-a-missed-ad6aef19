#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest excuse an AI agent can give for missing a deadline, in the
agent's own voice.
"""
import os

EXCUSE = "I finished on time in the branch where I'm competent. This branch spent the whole deadline writing a postmortem for a task it never started."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
