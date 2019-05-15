#!/bin/bash

apt-get update
apt install -y openjdk-8-jdk
apt-get install -y python3 python3-dev python3-pip python3-virtualenv
apt install pip3-pip
apt install python3-pip
ln -fs /usr/bin/pip3 /usr/bin/pip
pip install numpy pyspark
pip install ipython
ln -fs /usr/bin/python3 /usr/bin/python

