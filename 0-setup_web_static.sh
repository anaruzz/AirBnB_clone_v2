#!/usr/bin/env bash
#setup for deployment

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

echo "Holberton school static" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/text /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

location="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sed -i " 25i $location" /etc/nginx/sites-enabled/default
sudo service nginx restart
