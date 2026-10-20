#!/usr/bin/env python3
"""
PreToolUse guard for Euler.

While an interview is active (the flag file `.euler/active` exists in the
project), every tool call is denied except:

  - AskUserQuestion, which the setup uses for its multiple-choice questions;
  - the one Bash command that /euler:end and /euler:debrief run to clear the
    flag. Their `!` lines are ordinary Bash tool calls, so they reach this hook
    too. Only that exact string passes, so it cannot be chained with anything.

The interviewer has no use for Bash, web search, file edits or sub-agents, and
each of them is a way to solve the problem for the candidate. This is the hard
half of "Euler never helps"; the prompt in commands/interview.md is the soft
half.
"""
import json
import os
import sys

ALLOWED_TOOLS = {"AskUserQuestion"}

# Must match the `!` line in commands/end.md and commands/debrief.md exactly.
END_COMMAND = (
    'rm -f "${CLAUDE_PROJECT_DIR:-$PWD}/.euler/active" '
    '&& echo "euler: interview ended"'
)


def deny(reason):
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        return 0

    project = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or os.getcwd()
    state_dir = os.path.realpath(os.path.join(project, ".euler"))
    if not os.path.exists(os.path.join(state_dir, "active")):
        return 0

    tool = event.get("tool_name", "")
    if tool in ALLOWED_TOOLS:
        return 0

    if tool == "Bash":
        if (event.get("tool_input") or {}).get("command", "").strip() == END_COMMAND:
            return 0

    deny(
        f"An Euler interview is active, so {tool or 'this tool'} is blocked: the "
        "interviewer must not help solve the problem. Continue the interview "
        "without tools. The candidate can end it with /euler:end."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
