# Euler

A DSA interviewer for [Claude Code](https://code.claude.com). Euler runs a mock data-structures-and-algorithms interview and will not help you solve the problem.

## Install

```
/plugin marketplace add Kavya-24/euler
/plugin install euler@euler
```

## Use

- `/euler:interview [topic difficulty language]` starts an interview, for example `/euler:interview medium graphs python`. Euler asks only for what you leave out, then states one problem.
- `/euler:debrief` ends the interview and gives a verdict, scorecard, gaps, the better approach and a practice plan.
- `/euler:end` ends the interview without a debrief.

Full details are in [plugins/euler/README.md](plugins/euler/README.md).

## License

MIT
