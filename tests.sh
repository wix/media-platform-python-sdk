#!/usr/bin/env bash

virtualenv test-venv
source test-venv/bin/activate

pip install -e .

python setup.py test || exit 1
