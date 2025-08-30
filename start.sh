#!/bin/bash

#1 Step: build/rebuild container
docker build -t german_app .

#2 Step: force stop the previous version of the container
docker kill german_app || true
docker rm german_app || true

#3 Step: run new container
docker run -d \
    --name german_app \
    --network custom-network \
    --ip 10.0.0.103 \
    --entrypoint /docker-entrypoint.sh \
    german_app:latest
