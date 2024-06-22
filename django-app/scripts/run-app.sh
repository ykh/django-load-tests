#!/bin/bash

set -e

cd /src/app

python manage.py migrate

if [ "$DEBUG" = "True" ]; then
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn --bind 0.0.0.0:8000 --workers "$WSGI_WORKERS" app.wsgi:application
fi
