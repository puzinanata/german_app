FROM ubuntu:latest

ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/home/puzinanata/german_app

COPY / $APP_HOME

RUN cd $APP_HOME && \
  /bin/bash deployment/deploy_docker.sh
