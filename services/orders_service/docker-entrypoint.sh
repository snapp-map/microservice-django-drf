#!/usr/bin/env bash
set -euo pipefail

echo "ENTRYPOINT: Starting. CMD: $*"

PROJECT_DIR="/app"
cd "$PROJECT_DIR"

HOST="${DB_HOST:-db}"
PORT="${DB_PORT:-5432}"
echo "Waiting for database $HOST:$PORT ..."
until nc -z $HOST $PORT; do
  echo "Database is unavailable - sleeping"
  sleep 2
done
echo "Database is up!"

exec "$@"
