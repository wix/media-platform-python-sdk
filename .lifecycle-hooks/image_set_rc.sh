#!/bin/bash

sed -i "s/MEDIA_PLATFORM_SDK_VERSION/${RC_VERSION}/g" setup.py
git commit -a -m "CI: Set Version to ${RC_VERSION}"
git tag ${RC_VERSION}
git push origin ${RC_VERSION}
