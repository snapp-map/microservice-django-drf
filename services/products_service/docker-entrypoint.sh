#!/usr/bin/env bash
set -euo pipefail

echo "ENTRYPOINT: Starting. CMD: $*"

# مسیر پروژه را از محیط بگیرید یا پیش‌فرض '/app' است
PROJECT_DIR="${PROJECT_DIR:-/app}"

# Change to the project directory if it exists
if [ -d "$PROJECT_DIR" ]; then
  cd "$PROJECT_DIR"
else
  echo "Warning: PROJECT_DIR '$PROJECT_DIR' not found. Running from current dir."
fi

# Run migrations if manage.py exists in the project dir
if [ -f "manage.py" ]; then
  echo "Applying Django migrations..."
  python manage.py migrate --noinput
else
  echo "manage.py not found in project dir. Skipping migrations."
fi

echo "Starting server with: $@"
exec "$@"