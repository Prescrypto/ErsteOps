# ErsteOps
Operations for erste

# Vagrant

Initial setup

vagrant up --provision

Everyday usage

vagrant up

# Usage

This app is developed using python 3 , be aware to use pyton3 instead python

Run server:

python3 manage.py runserver [::]:8000

Migrate:
python3 manage.py migrate

etc, etc,..

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

# Decision tree

Requirments:

Add variable MEDIA_LOCAL=True to your env var

Use the end point:

https://<app>.herokuapp.com/decisiontree/upload/

to Upload decision tree from files located on:

Adult Symptoms:
https://github.com/Prescrypto/ErsteOps/blob/feature/decision_tree/tree_upload/adult_symptom_tree_2.csv

Pedriatic Symptoms
https://github.com/Prescrypto/ErsteOps/blob/feature/decision_tree/tree_upload/pedriatic_symptom_tree.csv


Create migrations(Here teh instruction jus as reference):

python3 manage.py dumpdata --format=json decisiontree > /vagrant/fixtures/decisiontree/initial_data.json



load migrations

python3 manage.py loaddata --database=default fixtures/decisiontree/initial_data.json


Check baisc functionality on vagrant:


In heroku:
https://<app>.herokuapp.com/decisiontree/searchsymptom/

