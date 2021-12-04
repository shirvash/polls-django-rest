#!/bin/sh

python app/manage.py migrate
python app/manage.py collectstatic --noinput
exec "$@"