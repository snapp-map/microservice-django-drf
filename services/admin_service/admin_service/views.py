from rest_framework.views import APIView
from rest_framework.response import Response
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


class AdminUsersView(APIView):
    def get(self, request):
        data = fetch_users()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)


class AdminProductsView(APIView):
    def get(self, request):
        data = fetch_products()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)


class AdminOrdersView(APIView):
    def get(self, request):
        data = fetch_orders()
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)


class AdminPaymentsView(APIView):
    def get(self, request):
        data = fetch_payments()
        serializer = PaymentSerializer(data, many=True)
        return Response(serializer.data)
