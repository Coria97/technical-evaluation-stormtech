FROM python:3.12-alpine

WORKDIR /usr/src/app

# Install Bash
RUN apk add --no-cache bash

# prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensure Python ouput is sent directly to the te terminal without
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["bash", "-e", "/usr/src/app/entrypoint.sh"]