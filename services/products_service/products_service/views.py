from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Custom permission: Admin can write, others can only read
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name", "price"]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at"]

    permission_classes = [IsAdminOrReadOnly]


# Internal API to reduce stock for Orders Service
@api_view(["PATCH"])
def reduce_stock(request, pk):
    """
    Reduce product stock for internal Orders Service calls.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    quantity = request.data.get("quantity")
    if quantity is None or int(quantity) < 1:
        return Response(
            {"error": "Invalid quantity"}, status=status.HTTP_400_BAD_REQUEST
        )

    if product.stock < int(quantity):
        return Response(
            {"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST
        )

    product.stock -= int(quantity)
    product.save()
    return Response({"id": product.id, "stock": product.stock})
