#!/bin/sh

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server
sudo sed -i -e "/bind-address/d" /etc/mysql/my.cnf
sudo service mysql restart

sudo mysqladmin password password
sudo mysql -uroot -ppassword mysql -e "CREATE DATABASE IF NOT EXISTS edseenTest; GRANT ALL PRIVILEGES ON edseenTest.* TO 'edseenTest'@'%' IDENTIFIED BY 'password';"
URL_DATABASE='mysql://root:password@localhost/edseenTest'

