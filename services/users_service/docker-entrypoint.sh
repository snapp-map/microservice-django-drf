#!/usr/bin/env bash
set -euo pipefail

echo "ENTRYPOINT: Starting. CMD: $*"

PROJECT_DIR="/app"

cd $PROJECT_DIR

if [ -f "manage.py" ]; then
  echo "Applying Django migrations..."
  python manage.py makemigrations --noinput
  python manage.py migrate --noinput
fi

echo "Starting server with: $@"
exec "$@"
