import requests
from django.conf import settings

USERS_SERVICE_URL = settings.USERS_SERVICE_URL
PRODUCTS_SERVICE_URL = settings.PRODUCTS_SERVICE_URL
ORDERS_SERVICE_URL = settings.ORDERS_SERVICE_URL
PAYMENTS_SERVICE_URL = settings.PAYMENTS_SERVICE_URL


# Fetch data from microservices
def fetch_users():
    try:
        resp = requests.get(f"{USERS_SERVICE_URL}/api/users/", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return []


def fetch_products():
    try:
        resp = requests.get(f"{PRODUCTS_SERVICE_URL}/api/products/", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return []


def fetch_orders():
    try:
        resp = requests.get(f"{ORDERS_SERVICE_URL}/api/orders/", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return []


def fetch_payments():
    try:
        resp = requests.get(f"{PAYMENTS_SERVICE_URL}/api/payments/", timeout=5)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return []
