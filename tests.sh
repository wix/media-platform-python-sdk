#!/usr/bin/env bash
set -x

python -m venv test-run
source test-run/bin/activate

python -m pip install -e .

python setup.py test || exit 1
