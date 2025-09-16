from rest_framework import serializers


# ==========================
# User Serializer
# ==========================
class UserSerializer(serializers.Serializer):
    """Serialize user data fetched from users-service."""

    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()


# ==========================
# Product Serializer
# ==========================
class ProductSerializer(serializers.Serializer):
    """Serialize product data fetched from products-service."""

    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


# ==========================
# Order Serializer
# ==========================
class OrderSerializer(serializers.Serializer):
    """Serialize order data fetched from orders-service."""

    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


# ==========================
# Payment Serializer
# ==========================
class PaymentSerializer(serializers.Serializer):
    """Serialize payment data fetched from payments-service."""

    id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
