#!/usr/bin/env bash
# Source: https://github.com/doccano/doccano/blob/master/tools/prod-django.sh

set -o errexit

echo "Initializing database"
python manage.py migrate

echo "Creating admin"
if [[ -n "${ADMIN_USERNAME}" ]] && [[ -n "${ADMIN_PASSWORD}" ]] && [[ -n "${ADMIN_EMAIL}" ]]; then
  python manage.py create_admin \
    --username "${ADMIN_USERNAME}" \
    --password "${ADMIN_PASSWORD}" \
    --email "${ADMIN_EMAIL}" \
    --noinput \
  || true
fi

echo "Starting django"
gunicorn --bind="0.0.0.0:${PORT:-8000}" --workers="${WORKERS:-4}" iheros.wsgi --timeout 300
