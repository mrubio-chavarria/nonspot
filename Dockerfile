FROM python:3.7-alpine

MAINTAINER Mario Rubio

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY . /code/

# EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

# ADD . /nonspot


RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps postgresql-dev build-base python-dev py-pip && \
 apk --purge del .build-deps

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip install Pillow

RUN python3 -m pip install -r requirements.txt --no-cache-dir

