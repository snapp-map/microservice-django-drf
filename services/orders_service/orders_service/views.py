from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .services.external_apis import validate_user, get_product


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Make a copy of the request data

        # Validate user exists via Users Service
        if not validate_user(data.get("user_id")):
            return Response(
                {"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Validate product exists via Products Service
        product = get_product(data.get("product_id"))
        if not product:
            return Response(
                {"error": "Product does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Calculate total_amount automatically
        data["total_amount"] = product["price"] * int(data.get("quantity", 1))

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
