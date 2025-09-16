from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.filters import SearchFilter, OrderingFilter
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

    # Filters: DjangoFilter, search, ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name", "price"]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "created_at"]

    # Permissions: Admin only for write, everyone can read
    permission_classes = [IsAdminOrReadOnly]
