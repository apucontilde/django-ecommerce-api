from rest_framework import serializers
from .models import Product, ProductCategory
from django.contrib.auth.models import User


class ProductSerializer(
    serializers.ModelSerializer
):  # create class to serializer model
    created_by = serializers.ReadOnlyField(source="created_by.username")
    categories = serializers.SlugRelatedField(
        many=True, queryset=ProductCategory.objects.all(), slug_field="name"
    )

    class Meta:
        model = Product
        fields = (
            "id",
            "short_name",
            "long_name",
            "sku",
            "price",
            "stock",
            "thumbnail",
            "physical_width",
            "physical_lenght",
            "physical_height",
            "categories",
            "created_by",
            "created_at",
            "updated_at",
        )


class UserSerializer(
    serializers.ModelSerializer
):  # create class to serializer user model
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "products")
