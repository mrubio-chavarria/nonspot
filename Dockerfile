
# Base image
FROM python:3.7-alpine

MAINTAINER Mario Rubio

# Set working directories
RUN mkdir /code
WORKDIR /code

# Add current directory code to working directory
ADD . /code/

# Set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV PORT=8000

# Install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# Install system dependencies
RUN apk add --no-cache gcc python3-dev musl-dev
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip3 install --no-cache-dir psycopg2 \
    && apk del --no-cache .build-deps
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps postgresql-dev build-base python-dev py-pip && \
 apk --purge del .build-deps
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip3 install Pillow
RUN pip3 install whitenoise
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Expose port
EXPOSE 8000

# Default command to listen
CMD exec gunicorn nonspot.wsgi:application --bind 0.0.0.0:8000 --workers 3
