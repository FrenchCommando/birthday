###########
# BUILDER #
###########

# pull official base image
FROM python:3.8.6-slim-buster

# set work directory
WORKDIR /usr/src/app

# lint
RUN pip install --upgrade pip setuptools
RUN pip install flake8
COPY . $WORKDIR
RUN flake8 --ignore=E121,E501,F401,W605 .

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:1339 --worker-class aiohttp.worker.GunicornWebWorker --timeout 300"
COPY . .

EXPOSE 1339

CMD [ "gunicorn", "host_page:init_app" ]
