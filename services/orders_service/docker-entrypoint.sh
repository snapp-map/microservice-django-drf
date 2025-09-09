#!/usr/bin/env bash
set -euo pipefail

# Enable trap for debugging in case of errors
trap 'echo "Error occurred in docker-entrypoint.sh at line $LINENO"; exit 1' ERR

# Dump current env for debugging (optional)
# echo "Starting entrypoint with Django settings module: ${DJANGO_SETTINGS_MODULE:-default}"

# If a custom entrypoint argument is provided, pass it through
# (This allows the CMD in Dockerfile to call: docker-entrypoint.sh python manage.py runserver ...)
if [ "$1" = "python" ]; then
  shift  # remove the 'python' arg
  # Optional: wait-for-db logic could go here if using a real DB
  :
fi

# 1) Apply migrations if database exists or migrations are defined
# You can uncomment the following block if you want migrations to run automatically on startup.
# Note: For SQLite this is usually fine; for other DBs you might want more robust checks.
if [ -f "manage.py" ]; then
  echo "Applying Django migrations..."
  python manage.py migrate --noinput
else
  echo "manage.py not found; skipping migrations."
fi

# 2) Collect static files (optional)
# Uncomment if you want to collect static at startup and you have STATIC_ROOT configured.
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# 3) Start the Django development server (or given command)
# If CMD passes additional args, they will be executed after this script finishes.
# We keep the original CMD behavior by executing the remaining arguments.
exec "$@"