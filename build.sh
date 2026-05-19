#!/usr/bin/env bash

pip install -r requirements.txt
echo "Running migrations..."
python manage.py migrate
python manage.py collectstatic --noinput
