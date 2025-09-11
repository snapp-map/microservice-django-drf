#!/bin/bash

echo "Waiting for database $USERS_DB_HOST:$USERS_DB_PORT ..."

while ! nc -z $USERS_DB_HOST $USERS_DB_PORT; do
  echo "Database is unavailable - sleeping"
  sleep 3
done

echo "Database is up - executing command"
exec "$@"
