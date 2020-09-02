# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apk update \
#     && apk add --no-cache gcc python3-dev musl-dev cairo \
#     && apk add libffi-dev libxml2-dev libxslt-dev \
#     && apk add postgresql \
#     && apk add postgresql-dev \
#     && apk add jpeg-dev zlib-dev libjpeg

# RUN pip install --upgrade pip \
#     && pip install Pillow \
#     && pip install cairosvg \
#     && pip install psycopg2 

RUN apk update && apk add --no-cache gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev libjpeg
    # && apk add libffi-dev libxml2-dev libxslt-dev libpango1.0-0 libpq-dev libcairo2
RUN apk add --no-cache \
    build-base cairo-dev cairo cairo-tools \
    # pillow dependencies
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install --upgrade pip 

RUN apk add --update --no-cache g++ gcc libxslt-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install Pillow
# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Docker for Python Developers
# https://mherman.org/presentations/dockercon-2018/#1
