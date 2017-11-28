#!/usr/bin/env bash

echo "==>Post DEPLOY Rules"

python ./chuko/manage.py migrate

echo "==> END postdeploy"