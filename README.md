# Gauntlex Python

A unified, sequential, project-based Python curriculum for [Gauntlex](https://github.com/Michealshodipo56/Gauntlex).

## Source repositories

| Source | Fork | License | Status |
| --- | --- | --- | --- |
| Exercism Python | [python-curriculum](https://github.com/Michealshodipo56/python-curriculum) | MIT | Import pending |
| 30 Days of Python | [30-Days-Of-Python](https://github.com/Michealshodipo56/30-Days-Of-Python) | Unverified | License review required before copying |
| C1 Code Crunch Convos | [C1-Code-Crunch-Convos](https://github.com/Michealshodipo56/C1-Code-Crunch-Convos) | GPL-3.0 | Copyleft compliance review required before copying |
| learn.python | [learn.python](https://github.com/Michealshodipo56/learn.python) | MIT | Import pending |

## Intended learning progression

1. Python foundations: variables, types, expressions, conditions, loops, functions
2. Strings, collections, recursion, algorithms and problem solving
3. Modules, files, errors, debugging and testing
4. OOP, typing, iterators, generators and decorators
5. Data structures, complexity and advanced algorithms
6. APIs, databases, concurrency and security fundamentals
7. Independent engineering projects and capstones

## Gauntlex compatibility

Each challenge needs a stable ID, original source and license metadata, prerequisites, learner-visible brief and starter code, a trusted server-side evaluator, and AI Auditor assessment criteria. Learners progress one challenge at a time, after passing both automated tests and an independent AI defense.

**Important:** Imported walkthroughs and reference solutions must not be exposed to the AI Guide or learner-facing application. Hidden tests must remain server-owned. Duplicate challenges will be curated by learning objective while retaining attribution.

## Current status

Repository initialized with the integration plan. **No source curriculum exercises have been imported or validated yet.**
## Build a source inventory

From the repository root (requires Git and Python 3.11+):

```bash
bash scripts/clone_sources.sh
```

This clones the four forks into ignored `sources/` directories and writes `curriculum/catalog.json`. The catalog is **not** an approved curriculum and contains no imported exercise bodies. Exercise boundaries outside Exercism are discovery candidates and need human review. Source checkout and script execution have not yet been verified in CI.
