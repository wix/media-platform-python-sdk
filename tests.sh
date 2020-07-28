#!/usr/bin/env bash
set -x

which python
which python3
python -V
python3 -V
python3.7 -V

python -m venv test-run
source test-run/bin/activate

python -m pip install -e .

python setup.py test || exit 1
