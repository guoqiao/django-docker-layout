#!/bin/bash
python manage.py migrate --noinput
python manage.py loaddata fixtures/initial_*.json
./sassc-compile.sh
# python manage.py runserver 0.0.0.0:8000
python manage.py yt_refresh_tokens
supervisord -n
