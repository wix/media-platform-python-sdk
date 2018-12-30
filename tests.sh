#!/usr/bin/env bash

virtualenv test-venv
source test-venv/bin/activate

pip install -r requirements.txt -r test-requirements.txt

python setup.py test || exit 1
