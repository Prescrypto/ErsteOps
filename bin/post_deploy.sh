#!/usr/bin/env bash

echo "==>Post DEPLOY Rules"

python ./ersteops/manage.py migrate

echo "==> END postdeploy"