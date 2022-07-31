#!/bin/sh
sleep 35
celery -A kanalservice_back beat -l info