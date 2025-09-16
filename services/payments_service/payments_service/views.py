from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from .models import Payment
from .serializers import PaymentSerializer
import requests

ORDERS_SERVICE_URL = "http://orders-service:8000/api/orders/"


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_id = serializer.validated_data["order_id"]

        # Fetch order info
        try:
            order_response = requests.get(f"{ORDERS_SERVICE_URL}{order_id}/", timeout=5)
            order_response.raise_for_status()
        except requests.RequestException:
            return Response(
                {"error": "Order not found or service unavailable"},
                status=status.HTTP_404_NOT_FOUND,
            )

        order_data = order_response.json()

        if float(order_data["total_amount"]) != float(
            serializer.validated_data["amount"]
        ):
            return Response(
                {"error": "Payment amount does not match order total"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            with transaction.atomic():
                payment = serializer.save(status="completed")

                # Optionally, update order status to 'paid'
                try:
                    requests.patch(
                        f"{ORDERS_SERVICE_URL}{order_id}/",
                        json={"status": "paid"},
                        timeout=5,
                    )
                except requests.RequestException:
                    raise Exception("Failed to update order status")

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
