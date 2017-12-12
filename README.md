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


# For windows
vagrant may throw the next error "unknown filesystem type 'vboxsf'"

Install the plugin:
vagrant plugin install vagrant-vbguest

Run server with Channels:

daphne ersteops.asgi:channel_layer --port 8000 -b 0.0.0.0

python3 manage.py runworker

