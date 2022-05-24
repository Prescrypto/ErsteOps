# ErsteOps
Operations for erste

# Vagrant

Initial setup

vagrant up --provision

Everyday usage

vagrant up


# Virtualenv

The app still use vagrant but for felxibility on deploying to heroku now the development are made using virtualenv, is more flexible

To create your venv:

`python3 -m venv env_2_2_ok`

Activate venv:

`cd /vagrant/env_2_2_ok;source bin/activate;cd /vagrant/ersteops`

Update pip if needed:

`python -m pip install --upgrade pip`

Install requirments:

`pip install -r /vagrant/requirements.txt`


# Usage 

- Activate python venv.
- Start yarn:

`yarn dev`

- Start daphne server:

```
$ cd /vagrant/ersteops
$ daphne ersteops.asgi:application --port 8000 -b 0.0.0.0
```

- Start django server:

```
$ cd /vagrant/ersteops
$ python manage.py runworker channels --settings=ersteops.settings -v3 --traceback
```

# Front End

The front-end's interactive elements are composed with Vue. The javascript is compiled by Webpack and integrated with Django using `django-webpack-loader`.

To add a new bundle, add a new named entry to the `entry` collection in `webpack.config.js`. Then require it in Django with:

```
{% load render_bundle from webpack_loader %}
{% render_bundle 'entry_name' %}
```

- Install dependencies:

`yarn install`

- Development server:

`yarn dev`

- Build production assets:

`NODE_ENV=production yarn build`

# For windows
vagrant may throw the next error "unknown filesystem type 'vboxsf'"

Install the plugin:
vagrant plugin install vagrant-vbguest

Run server with Channels:
install redis server:
sudo apt-get install redis-server

Run Redis
daphne ersteops.asgi:channel_layer --port 8000 -b 0.0.0.0

python3 manage.py runworker

# Drop Database if neccesary
In vagrant box go to /vagrant/ersteops and type the follow:

```
$ sudo -i -u postgres psql -c "DROP DATABASE mydb"
$ sudo -i -u postgres psql -c "CREATE DATABASE mydb"
$ python3 manage.py migrate
$ python3 manage.py loaddata ../fixtures/auth/initial_data.json
$ python3 manage.py loaddata ../fixtures/auth/test_data.json

```

HINT: Use in case have a lot of test with db or have change migrations file missing references


# Enable python setup on heroku stack20
source /vagrant/venv/bin/activate