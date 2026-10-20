---
description: End the Euler interview and lift the tool restrictions
disable-model-invocation: true
allowed-tools: Bash(rm:*), Bash(echo:*)
---

!`rm -f "${CLAUDE_PROJECT_DIR:-$PWD}/.euler/active" && echo "euler: interview ended"`

The interview is over and the tool restrictions are lifted. Say so in one line. If no debrief has been given yet, offer one with `/euler:debrief`. Do not discuss the problem or the candidate's solution unless they ask.
