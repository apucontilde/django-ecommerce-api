from django_filters import rest_framework as filters
from .models import Product


# We create filters for each field we want to be able to filter on
class ProductFilter(filters.FilterSet):
    short_name = filters.CharFilter(lookup_expr="icontains")
    long_name = filters.CharFilter(lookup_expr="icontains")
    price_gt = filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_lte = filters.NumberFilter(field_name="price", lookup_expr="lte")
    stock_gt = filters.NumberFilter(field_name="stock", lookup_expr="gte")
    stock_lte = filters.NumberFilter(field_name="stock", lookup_expr="lte")
    category = filters.CharFilter(field_name="categories__name", lookup_expr="iexact")

    class Meta:
        model = Product
        fields = (
            "short_name",
            "long_name",
            "sku",
            "price_gt",
            "price_lte",
            "stock_gt",
            "stock_lte",
            "category",
        )
