FROM ubuntu:latest
LABEL org.opencontainers.image.authors="Tim Miller <timmillergcpuser@gmail.com>"

RUN apt-get update
RUN apt-get -y install nginx
COPY index.html /var/www/html/index.html
COPY nginx-site-default /etc/nginx/sites-enabled/default

CMD ['nginx','-g','daemon off;']
EXPOSE 80
