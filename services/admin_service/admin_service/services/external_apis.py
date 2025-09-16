import requests
from django.conf import settings


# ==========================
# Fetch Users from users-service
# ==========================
def fetch_users():
    """Fetch all users from the users-service API."""
    try:
        response = requests.get(f"{settings.USERS_SERVICE_URL}/api/users/", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.RequestException:
        return []


# ==========================
# Fetch Products from products-service
# ==========================
def fetch_products():
    """Fetch all products from products-service."""
    try:
        response = requests.get(
            f"{settings.PRODUCTS_SERVICE_URL}/api/products/", timeout=5
        )
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.RequestException:
        return []


# ==========================
# Fetch Orders from orders-service
# ==========================
def fetch_orders():
    """Fetch all orders from orders-service."""
    try:
        response = requests.get(f"{settings.ORDERS_SERVICE_URL}/api/orders/", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.RequestException:
        return []


# ==========================
# Fetch Payments from payments-service
# ==========================
def fetch_payments():
    """Fetch all payments from payments-service."""
    try:
        response = requests.get(
            f"{settings.PAYMENTS_SERVICE_URL}/api/payments/", timeout=5
        )
        response.raise_for_status()
        data = response.json()
        # Normalize to list
        if isinstance(data, list):
            return data
        return data.get("results", [])
    except requests.RequestException:
        return []
