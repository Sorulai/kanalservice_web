FROM python:3.10-alpine
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint.sh

COPY ./entrypoint_celery.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint_celery.sh

COPY ./entrypoint_celery_beat.sh /usr/src/app/
RUN chmod +x /usr/src/app/entrypoint_celery_beat.sh

COPY . /usr/src/app/
