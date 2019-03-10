#!/bin/bash
#
# boot.sh
#
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - outpost-calc-web:app
