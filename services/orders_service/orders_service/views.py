import requests
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

# Base URL for Products Service API
PRODUCTS_SERVICE_URL = "http://products-service:8002/api/products/"


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        # 1. Fetch product details from Products Service
        try:
            product_response = requests.get(
                f"{PRODUCTS_SERVICE_URL}{product_id}/", timeout=5
            )
            product_response.raise_for_status()
        except requests.RequestException:
            return Response(
                {"error": "Product not found or service unavailable"},
                status=status.HTTP_404_NOT_FOUND,
            )

        product_data = product_response.json()

        # 2. Validate available stock
        if product_data["stock"] < quantity:
            return Response(
                {"error": "Not enough stock"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 3. Calculate total order amount
        total_amount = float(product_data["price"]) * quantity

        # 4. Wrap order creation in a database transaction
        try:
            with transaction.atomic():
                # Create the order in Orders DB
                order = Order.objects.create(
                    user_id=user_id,
                    product_id=product_id,
                    quantity=quantity,
                    total_amount=total_amount,
                )

                # 5. Update product stock in Products Service
                try:
                    patch_response = requests.patch(
                        f"{PRODUCTS_SERVICE_URL}{product_id}/",
                        json={"stock": product_data["stock"] - quantity},
                        timeout=5,
                    )
                    patch_response.raise_for_status()
                except requests.RequestException:
                    # If stock update fails, raise an exception to trigger rollback
                    raise Exception("Failed to update product stock")

        except Exception as e:
            # Transaction is rolled back automatically if an exception is raised
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # 6. Return the created order if everything succeeded
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
