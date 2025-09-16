import requests
from django.conf import settings


# ==========================
# Fetch Users
# ==========================
def fetch_users():
    """Fetch all users from users-service API."""
    try:
        url = f"{settings.USERS_SERVICE_URL}/api/users/"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # Always return a list
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        elif isinstance(data, list):
            return data
        return []
    except requests.RequestException:
        return []


# ==========================
# Fetch Products
# ==========================
def fetch_products():
    """Fetch all products from products-service API."""
    try:
        url = f"{settings.PRODUCTS_SERVICE_URL}/api/products/"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        elif isinstance(data, list):
            return data
        return []
    except requests.RequestException:
        return []


# ==========================
# Fetch Orders
# ==========================
def fetch_orders():
    """Fetch all orders from orders-service API."""
    try:
        url = f"{settings.ORDERS_SERVICE_URL}/api/orders/"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        elif isinstance(data, list):
            return data
        return []
    except requests.RequestException:
        return []


# ==========================
# Fetch Payments
# ==========================
def fetch_payments():
    """Fetch all payments from payments-service."""
    try:
        url = f"{settings.PAYMENTS_SERVICE_URL}/api/payments/"
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        # Payments-service returns {"count": ..., "results": [...]}
        if isinstance(data, dict) and "results" in data:
            return data["results"]
        elif isinstance(data, list):
            return data
        return []
    except requests.RequestException:
        return []
