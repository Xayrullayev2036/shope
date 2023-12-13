from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ["created_at", "updated_at"]


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
