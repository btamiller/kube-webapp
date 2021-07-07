#!/bin/bash

buildah from --name testwa-backend ubuntu:latest
buildah run testwa-backend -- apt-get update
buildah run testwa-backend -- apt-get -y upgrade
buildah run testwa-backend -- apt-get -y install uwsgi uwsgi-plugins-all fortune-mod fortunes
buildah copy testwa-backend dothecow.py /var/www/wsgi-bin/
buildah config --cmd "uwsgi --plugin http --plugin python3 --http :9090 --uid 33 --gid 33 --wsgi-file /var/www/wsgi-bin/dothecow.py --master --processes 4 --threads 2" testwa-backend
buildah config --author "Tim Miller <timmillergcpuser@gmail.com>" testwa-backend

buildah commit testwa-backend testwa-backend
