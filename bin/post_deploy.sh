#!/usr/bin/env bash

echo "==>Post DEPLOY Rulezz"
python ./ersteops/manage.py migrate

python ./ersteops/manage.py loaddata fixtures/auth/initial_data.json

python ./ersteops/manage.py loaddata fixtures/auth/test_data.json
echo "==> END postdeploy"
