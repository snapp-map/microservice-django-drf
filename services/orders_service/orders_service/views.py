from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
import requests


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

        try:
            with transaction.atomic():
                # Create order
                order = serializer.save()

                # Reduce stock using internal Products API
                patch_response = requests.patch(
                    f"http://products-service:8000/api/products/{order.product_id}/reduce-stock/",
                    json={"quantity": quantity},
                    timeout=5,
                )

                patch_response.raise_for_status()

        except requests.RequestException as e:
            return Response(
                {"error": "Failed to update product stock"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
