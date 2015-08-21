FROM python:2.7
MAINTAINER Guo Qiao "guoqiao@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y libmysqlclient-dev wget git

WORKDIR /tmp

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

ADD requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /app

EXPOSE 8000
