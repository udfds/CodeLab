FROM python:3.7-alpine

LABEL MAINTAINER="Diego Souza <dfds@outlook.com>"

COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt
ADD . /var/www/
WORKDIR /var/www/
