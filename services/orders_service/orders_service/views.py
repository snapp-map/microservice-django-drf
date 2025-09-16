# orders/views.py
from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .services.external_apis import get_product


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quantity = serializer.validated_data["quantity"]
        product_data = serializer.product_data

        # Check stock
        if product_data["stock"] < quantity:
            return Response(
                {"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Atomic transaction
        try:
            with transaction.atomic():
                # Create order
                order = serializer.save()

                # Reduce stock in Products Service
                import requests

                try:
                    patch_response = requests.patch(
                        f"http://products-service:8002/api/products/{order.product_id}/",
                        json={"stock": product_data["stock"] - quantity},
                        timeout=5,
                    )
                    patch_response.raise_for_status()
                except requests.RequestException:
                    raise Exception("Failed to update product stock")

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
