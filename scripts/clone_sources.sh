#!/usr/bin/env bash
set -euo pipefail
mkdir -p sources
git clone https://github.com/Michealshodipo56/python-curriculum.git sources/exercism
git clone https://github.com/Michealshodipo56/30-Days-Of-Python.git sources/thirty-days
git clone https://github.com/Michealshodipo56/C1-Code-Crunch-Convos.git sources/c1
git clone https://github.com/Michealshodipo56/learn.python.git sources/learn
python3 scripts/build_catalog.py
