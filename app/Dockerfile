FROM ubuntu:18.04 AS base
WORKDIR /opt
RUN apt update && apt-get -y install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update
RUN apt-get install -y python3.6
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
RUN apt-get install -y python3-pip locales
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
