#!/usr/bin/env bash
set -euo pipefail

echo "ENTRYPOINT: Starting. CMD: $*"

PROJECT_DIR="/app"
cd "$PROJECT_DIR"

# صبر کردن برای آماده شدن دیتابیس
HOST="${DB_HOST:-db}"
PORT="${DB_PORT:-5432}"
echo "Waiting for database $HOST:$PORT ..."
until nc -z $HOST $PORT; do
  echo "Database is unavailable - sleeping"
  sleep 2
done
echo "Database is up!"

# اجرای migrate ها
echo "Running makemigrations..."
python manage.py makemigrations --noinput || true

echo "Applying migrations..."
python manage.py migrate --noinput

# اجرای سرور
echo "Starting server with: $@"
exec "$@"
