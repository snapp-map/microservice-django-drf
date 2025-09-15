import requests
from django.conf import settings

USERS_SERVICE_URL = settings.USERS_SERVICE_URL
PRODUCTS_SERVICE_URL = settings.PRODUCTS_SERVICE_URL


def validate_user(user_id):
    response = requests.get(f"{USERS_SERVICE_URL}/users/{user_id}/")
    if response.status_code == 200:
        return True
    return False


def get_product(product_id):
    response = requests.get(f"{PRODUCTS_SERVICE_URL}/products/{product_id}/")
    if response.status_code == 200:
        return response.json()
    return None
