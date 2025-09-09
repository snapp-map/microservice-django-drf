#!/bin/bash

docker-compose exec users-service python manage.py makemigrations --noinput
docker-compose exec users-service python manage.py migrate --noinput

docker-compose exec products-service python manage.py makemigrations --noinput
docker-compose exec products-service python manage.py migrate --noinput

docker-compose exec orders-service python manage.py makemigrations --noinput
docker-compose exec orders-service python manage.py migrate --noinput

docker-compose exec payments-service python manage.py makemigrations --noinput
docker-compose exec payments-service python manage.py migrate --noinput