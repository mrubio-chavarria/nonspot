
# Base image
FROM python:3.7-stretch

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
RUN pip3 install Pillow
RUN pip3 install whitenoise
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Expose port
EXPOSE 8000



# Default command to listen
CMD exec gunicorn nonspot.wsgi:application --bind 0.0.0.0:8000 --workers 3
