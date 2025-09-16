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
            data = fetch_users()
            serializer = UserSerializer(data, many=True)
            serializer.is_valid(raise_exception=True)
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
            data = fetch_products()
            serializer = ProductSerializer(data, many=True)
            serializer.is_valid(raise_exception=True)
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
            data = fetch_orders()
            serializer = OrderSerializer(data, many=True)
            serializer.is_valid(raise_exception=True)
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
            # Fetch payments from payments-service
            results = fetch_payments()  # should always return a list
            if not isinstance(results, list):
                # Safety fallback
                results = []

            # Correctly pass data= to serializer
            serializer = PaymentSerializer(data=results, many=True)
            serializer.is_valid(raise_exception=True)  # validate data
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
