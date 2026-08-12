# Roadmap — vitalic-static-assets

<!-- CONTRACT — see the "Roadmap" section of CLAUDE.md.
     This is the HIGH-LEVEL layer: a handful of objectives, each with a falsifiable
     "Done when". Tactical detail belongs in BACKLOG.md and is linked rather than copied.
     NOTE: this repository is PUBLIC. Everything in this file is world-readable — keep it
     to what this repo is and does, and out of anything internal.
     Dates are ISO, Australia/Brisbane. -->

| | |
|---|---|
| **Owner** | Luke McKenzie |
| **Reviewed** | 2026-08-13 |
| **Review by** | 2026-11-13 |
| **Confirmed by owner** | **No — drafted 2026-08-13 from this repo's own evidence, awaiting Luke's confirmation.** See the note below |
| **Tactical detail** | [`BACKLOG.md`](../BACKLOG.md) — small chores, one per line with a size tag |
| **Business rendering** | None of its own — this repo is a shared asset store, not a system with its own explainer |

> **Read the confirmation status before treating this as direction.** The objectives below
> are drawn from what this repo already records rather than from a stated priority. They are
> a proposal. **Do not rank work against this file until `Confirmed by owner` says yes.**
>
> **This repository is public.** Unlike every other roadmap in the estate, this file can be
> read by anyone. Keep it to this repo's own scope; internal detail belongs in a private
> repo, not here.

## Now

### 1. Stay a reliable canary for the automated review-and-merge pipeline

**Why it matters.** This repo is the designated first repo for changes to the shared dev
pipeline — see [`docs/PIPELINE.md`](PIPELINE.md) — and it was chosen for exactly one reason:
it has the lowest blast radius in the estate. No deployment, no runtime, no dependencies,
one asset. It is also the repo whose name is hard-coded through the pipeline's own test
fixtures, so its shape is an assumption other things are built on. A canary that stops
resembling a normal repo, or that grows something worth breaking, stops being a useful test.

**Done when.** All four hold, checked whenever CI or repo settings change:

- `ci.yml` still triggers on `pull_request` **and** `push: main`, and still gates on the two
  jobs `gitleaks` and `test`, under those exact names.
- The `test` job still hard-requires the published asset to exist, still enforces the 2 MB
  ceiling, and still validates every SVG as well-formed XML.
- No deploy step, no production credential, and no long-lived secret has been added to this
  repo — its value as a canary depends on there being nothing here worth losing.
- The repo still contains no application code, so a pipeline change tested here is testing
  the general case rather than a special one.

**As at 2026-08-13.** All four hold. CI runs `gitleaks` + `test`; there is no deploy
workflow and no repository secret in use.

### 2. Be a usable brand-asset source of truth, or stop being described as one

**Why it matters.** Other Vitalic projects each carry their own copy of several brand
variants while describing this repository as where those assets come from. This repository
currently publishes **one** variant. A source-of-truth claim that holds for one file out of
several is worse than no claim at all: it tells a reader the sync is someone's job when in
practice nothing syncs, and the copy actually being rendered is not the copy here.

**Done when.** Either arm closes it — but one of them must:

- the brand variants Vitalic's own surfaces actually render are published here, so the claim
  becomes true and the raw-URL contract is worth pointing at; **or**
- the "source of truth" wording is removed from the projects that make it, so no one is
  relying on a sync that does not exist.

Leaving it half-true is the one outcome that does not count as done.

**This is a decision, not a chore — it needs Luke.** This repository is public. Publishing a
further brand asset here makes that asset world-readable, permanently and by design, which
is a deliberate choice about what Vitalic puts in the open rather than a tidy-up an agent
should make on its own. The second arm — withdrawing the claim — needs no publication
decision and is available at any time, which is worth knowing if the first arm stalls.

**As at 2026-08-13.** One asset published. The claim is outstanding.

## Next

Nothing queued. Small hygiene items live in [`BACKLOG.md`](../BACKLOG.md) and do not need to
be lifted to this file.

## Later

Nothing queued.

## Keeping this honest

Three rules, repeated here so they hold even when this file is read on its own:

1. A PR that satisfies a **Done when** updates this file in the same diff.
2. Keep this file inside this repo's own scope. It is public, and it is the only roadmap in
   the estate that is — nothing internal belongs here.
3. When every objective under **Now** is done, or today is past **Review by**, say so and
   ask Luke what comes next. Do not invent the next objective — and note this file is
   **unconfirmed**, so the first thing to ask for is confirmation, not more objectives.
