#!/bin/bash

buildah from --name testwa-frontend ubuntu:latest
buildah run testwa-frontend -- apt-get update
buildah run testwa-frontend -- apt-get install nginx
buildah copy testwa-frontend index.html /var/www/html/index.html
buildah copy testwa-frontend nginx-site-default /etc/nginx/sites-enabled/default

buildah config --author "Tim Miller <timmillergcpuser@gmail.com>" testwa-frontend
buildah config --port 80 testwa-frontend
buildah config --cmd "nginx -g 'daemon off;'" testwa-frontend

buildah commit testwa-frontend testwa-frontend
