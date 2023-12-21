from django_filters import rest_framework as filters
from .models import Order


# We create filters for each field we want to be able to filter on
class OrderFilter(filters.FilterSet):
    user = filters.CharFilter(field_name="user__username", lookup_expr="iexact")

    class Meta:
        model = Order
        fields = ("user",)
