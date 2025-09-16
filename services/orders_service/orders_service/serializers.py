from rest_framework import serializers
from .models import Order
from .services.external_apis import validate_user, get_product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("total_amount", "status", "created_at")

    def validate_user_id(self, value):
        if not validate_user(value):
            raise serializers.ValidationError("User does not exist")
        return value

    def validate_product_id(self, value):
        product = get_product(value)
        if not product:
            raise serializers.ValidationError("Product does not exist")
        self.product_data = product  # store product info for later
        return value

    def create(self, validated_data):
        # Calculate total amount using stored product data
        product_price = float(self.product_data["price"])
        quantity = validated_data["quantity"]
        validated_data["total_amount"] = product_price * quantity
        return super().create(validated_data)
