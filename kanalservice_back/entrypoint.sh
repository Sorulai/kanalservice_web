#!/bin/sh
sleep 15
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn kanalservice_back.wsgi:application --bind 0.0.0.0:8080