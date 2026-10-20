# Euler

A DSA interviewer for Claude Code. Euler runs a mock data-structures-and-algorithms interview, and it will not help you solve the problem.

## Commands

### `/euler:interview [pre-fill]`

Starts a DSA interview. Euler asks only for a **topic**, **difficulty** and **language** (skipped if you pass them), then states one problem. Defaults: one problem, about 30 minutes, no hints.

During the interview Euler answers clarifying questions about the problem, probes your approach, complexity and edge cases, and keeps a private scorecard. It gives no hints, patterns, or solutions, and does not say whether your approach is right.

### `/euler:debrief`

After the interview: a verdict, a score per criterion, strengths, gaps, the better approach to each problem, and a practice plan. This is the only place Euler teaches. Running it also ends the interview and lifts the tool restrictions.

### `/euler:end`

Ends the interview and lifts the tool restrictions without a debrief.

## How "no help" is enforced

- **Prompt (soft):** the rules in `commands/interview.md`.
- **Hook (hard):** `hooks/interview_guard.py` is a `PreToolUse` hook. While `.euler/active` exists it denies every tool except `AskUserQuestion`, so Euler cannot run code, search the web, or edit files for you.

If a session dies with the interview still active, tools stay blocked in that project until you run `/euler:end` or delete `.euler/active`.

## Notes

- Add `.euler/` to your `.gitignore`; it holds the `active` flag.
- Built for self-practice. It is not designed or validated for evaluating real candidates.
