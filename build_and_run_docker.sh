#!/bin/sh

docker build -t birthdaybuild .
docker run -p 1339:1339 birthdaybuild
