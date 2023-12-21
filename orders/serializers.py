from rest_framework import serializers
from .models import Order, Product


class OrderSerializer(serializers.ModelSerializer):  # create class to serializer model
    user = serializers.ReadOnlyField(source="user.username")
    products = serializers.HyperlinkedRelatedField(
        many=True, queryset=Product.objects.all(), view_name="get_delete_update_product"
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "shipping_address_line_1",
            "shipping_address_line_2",
            "shipping_country",
            "shipping_state_province",
            "shipping_city",
            "shipping_postal_code",
            "billing_address_line_1",
            "billing_address_line_2",
            "billing_country",
            "billing_state_province",
            "billing_city",
            "billing_postal_code",
            "line_total",
            "shipping_total",
            "tax_total",
            "dicounted_total",
            "shipped",
            "tracking_reference",
            "products",
            "user",
        )
