#!/bin/bash
set -x

git tag ${RC_VERSION}
git push origin ${RC_VERSION}
