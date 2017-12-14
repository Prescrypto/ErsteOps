#!/usr/bin/env bash

echo "=> Start config box..."
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y build-essential libssl-dev wget python-pip python-dev libffi-dev
sudo pip install -U pip

# Install PostgreSQL
echo "Installing postgresql"
sudo apt-get install -y libpq-dev postgresql postgresql-contrib libxml2-dev libxslt1-dev zlib1g-dev build-essential libssl-dev libffi-dev
# Create database if not exist
sudo -i -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname = 'mydb'" | grep -q 1 || sudo -i -u postgres psql -c "CREATE DATABASE mydb"

# Create user
echo "Creating user and granting privileges"
sudo -i -u postgres psql -c "CREATE USER vagrant WITH PASSWORD 'vagrant';"
sudo -i -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mydb TO vagrant;"

echo "=> Installing requirements..."
sudo pip install -r /vagrant/requirements.txt

echo "Install Python 3"
sudo apt-get install -y python3

echo "Install Python 3 dev"
sudo apt-get install -y python3-dev

echo "Install pip3"
sudo apt-get install -y python3-pip

echo "Install pip3 requirements"
sudo pip3 install -r /vagrant/requirements.txt

echo "setuptools"
sudo pip3 install -vU setuptools

echo "nodejs"
sudo apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

echo "yarn"
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E074D16EB6FF4DE3
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get install -y apt-transport-https
sudo apt-get update && sudo apt-get install -y yarn

echo "nodejs dependencies"
cd /vagrant && yarn

echo "=> End config box..."
