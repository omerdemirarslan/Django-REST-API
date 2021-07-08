FROM python:3.9

LABEL maintainer="omerdemirarsln@gmail.com"

ENV PYTHONUNBUFFERED 1

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 5000
