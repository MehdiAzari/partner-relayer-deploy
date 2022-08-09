#!/bin/sh

docker-compose -f docker-compose.yaml up --scale endpoint=1 --remove-orphans -d
