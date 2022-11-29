FROM python:3.10.5-slim

RUN #apt update && apt install -y --no-install-recommends default-jre

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
#ENV JAVA_HOME=/usr/lib/jvm/java-l1-openjdk-amd64

CMD [ "tail", "-f", "/dev/null"  ]