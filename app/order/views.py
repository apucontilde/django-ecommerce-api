from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from api.pagination import CustomPagination
from .models import Order
from .serializers import OrderSerializer
from .filters import OrderFilter


class ListCreateOrderAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    def perform_create(self, serializer):
        # Assign the user who created the product
        serializer.save(created_by=self.request.user)


class RetrieveUpdateDestroyOrderAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
