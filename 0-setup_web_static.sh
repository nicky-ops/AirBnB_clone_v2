#!/usr/bin/env bash
# This script sets up a webserver for the deployment of a static website
if ! command -v ngnix &> /dev/null; then
	sudo apt-get update
	sudo apt-get install nginx
fi

sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

echo "<html>
<head>
	<title> Test Page </title>
</head>
<body>
	<h1>This is a test page</h1>
	<p> This page is used to test configuration. </p>
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config

sudo service nginx restart

