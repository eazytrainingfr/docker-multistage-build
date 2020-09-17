FROM ubuntu:16.04 AS base
WORKDIR /opt
RUN apt-get update && apt-get install -y python3 python3-pip locales
COPY requirements.txt /opt
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN pip3 install -r requirements.txt

FROM base as src
COPY . /opt

FROM src as test
COPY requirements.dev.txt /opt
RUN pip3 install -r requirements.dev.txt
RUN python3 -m pytest

FROM src as prod
ENTRYPOINT FLASK_APP=/opt/app.py FLASK_RUN_PORT=8080 flask run --host=0.0.0.0
