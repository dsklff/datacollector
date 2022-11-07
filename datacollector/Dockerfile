# pull official base image
FROM python:3.7.3-alpine
# set work directory
WORKDIR /datacollector
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev

RUN apk add --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    pip install --no-cache-dir cryptography==3.2.1 && \
    apk del \
        libressl-dev \
        musl-dev \
        libffi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install Pillow
COPY ./entrypoint.sh .
# copy project
COPY . /datacollector

ENTRYPOINT ["./entrypoint.sh"]

