#!/bin/sh

sudo apt-get update
sudo apt-get -y install wget apache2

wget https://raw.githubusercontent.com/edseen/cloud-aware/master/challenge03/index.html
sudo cp index.html /var/www/html/
