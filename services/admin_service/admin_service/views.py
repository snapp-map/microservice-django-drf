from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.external_apis import (
    fetch_users,
    fetch_products,
    fetch_orders,
    fetch_payments,
)
from .serializers import (
    UserSerializer,
    ProductSerializer,
    OrderSerializer,
    PaymentSerializer,
)


# ==========================
# Admin Users View
# ==========================
class AdminUsersView(APIView):
    """Admin view to list all users."""

    def get(self, request):
        try:
            results = fetch_users()  # لیست دیکشنری
            serializer = UserSerializer(results, many=True)  # بدون data=
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


# ==========================
# Admin Products View
# ==========================
class AdminProductsView(APIView):
    """Admin view to list all products."""

    def get(self, request):
        try:
            results = fetch_products()
            serializer = ProductSerializer(results, many=True)  # بدون data=
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


# ==========================
# Admin Orders View
# ==========================
class AdminOrdersView(APIView):
    """Admin view to list all orders."""

    def get(self, request):
        try:
            results = fetch_orders()
            serializer = OrderSerializer(results, many=True)  # بدون data=
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


# ==========================
# Admin Payments View
# ==========================
class AdminPaymentsView(APIView):
    """Admin view to list all payments."""

    def get(self, request):
        try:
            results = fetch_payments()  # باید همیشه لیست برگرداند
            serializer = PaymentSerializer(results, many=True)  # بدون data=
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
