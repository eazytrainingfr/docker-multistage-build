# Étape 1 : Base Python
FROM ubuntu:18.04 AS base
WORKDIR /opt

RUN apt update && \
    apt-get -y install software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.6 python3-pip locales && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1 && \
    locale-gen en_US.UTF-8

COPY requirements.txt /opt
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

RUN pip3 install -r requirements.txt

# Étape 2 : Copie du code source
FROM base AS src
COPY . /opt

# Étape 3 : Tests
FROM src AS test
COPY requirements.dev.txt /opt
RUN pip3 install -r requirements.dev.txt && \
    python3 -m pytest

# Étape 4 : Production
FROM src AS prod
ENV FLASK_APP=/opt/app.py \
    FLASK_RUN_PORT=8080
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
