#!/bin/sh
sleep 25
celery -A kanalservice_back worker -l info