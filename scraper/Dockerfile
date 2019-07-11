FROM python:3.6

ENV PYTHONUNBUFFERED 1

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app

ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

ADD . /app
WORKDIR /app

RUN pip install  -r requirements.txt

ENTRYPOINT ["dumb-init", "--"]