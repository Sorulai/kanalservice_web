#!/bin/sh
sleep 30
celery -A kanalservice_back worker -l info