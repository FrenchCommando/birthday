#!/bin/sh

docker build -t birthdaybuild .
docker run -d --rm -p 1339:1339 birthdaybuild
