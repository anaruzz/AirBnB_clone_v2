#!/usr/bin/env bash
#setup for deployment

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo -e "$content"| sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '42i location /hbnb_static {\n alias /data/web_static/current;\n}' /etc/nginx/sites-enabled/default
sudo service nginx restart
