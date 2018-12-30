#!/bin/bash

sed -i "s/MEDIA_PLATFORM_SDK_VERSION/${RC_VERSION}/g" setup.py
git tag ${RC_VERSION}
git push origin ${RC_VERSION}
