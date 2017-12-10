#!/usr/bin/env bash

echo "==>Post DEPLOY Rules"

python ./ersteops/manage.py migrate
yarn build

echo "==> END postdeploy"
