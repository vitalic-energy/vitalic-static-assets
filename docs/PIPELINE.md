# Hermes Dev Pipeline

This repository is wired into the Hermes autonomous dev pipeline. Changes flow
through the following loop: an issue is opened, a Kanban card is created for
it, an isolated Claude Code worker picks up the card and implements the
change, the worker opens a pull request, the PR auto-merges once checks are
green, and the loop closes back to the originating issue.

Auto-merge is governed by a checks-only policy for non-critical repositories
like this one; see [ADR 0009](https://github.com/vitalic-energy/vitalic-hermes-infra/blob/main/docs/decisions/0009-checks-only-auto-merge-non-critical.md)
in the infra repo for the full policy.
