#!/usr/bin/env bash

echo "==>Post DEPLOY Rules"
python ./ersteops/manage.py migrate

python ./ersteops/manage.py loaddata fixtures/auth/initial_data.json

python ./ersteops/manage.py loaddata fixtures/auth/test_data.json.json
echo "==> END postdeploy"
