#!/bin/bash

sudo yum -y install which java-1.8.0-openjdk
sudo echo "export JAVA_HOME=$(dirname $(dirname $(readlink -f $(type -P java))))" > /etc/profile.d/javahome.sh
