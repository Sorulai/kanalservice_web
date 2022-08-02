#!/bin/sh
sleep 40
celery -A kanalservice_back beat -l info