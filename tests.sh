#!/usr/bin/env bash

python3 -m venv test-run
source test-run/bin/activate

pip install -e .

python3 setup.py test || exit 1
