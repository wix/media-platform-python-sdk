#!/bin/bash

DST_TAG="release-${RC_VERSION}"
git tag ${DST_TAG}
git push origin ${DST_TAG}
