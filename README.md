# Ecommerce Microservices with Django DRF (Docker Compose)

A minimal, runnable set of Django DRF microservices (Users, Products, Orders, Payments) orchestrated via Docker Compose.

## Architecture
- **Each service**: Django + Django REST Framework
- **Inter-service communication**: REST over HTTP
- **Data**: PostgreSQL (each service can have its own database)
- **Configuration management**: environment variables in Docker Compose
- **Cache/Queues**: Redis (optional)

## Prerequisites
- Docker Engine
- Docker Compose

## Quick Start

1) **Clone the entire project**

2) **Build and run with Docker Compose**

```bash  
docker-compose up --build  