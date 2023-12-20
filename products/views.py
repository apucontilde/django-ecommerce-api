from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Product
from .serializers import productserializer
from .pagination import CustomPagination
from .filters import ProductFilter


class ListCreateProductAPIView(ListCreateAPIView):
    serializer_class = productserializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def perform_create(self, serializer):
        # Assign the user who created the product
        serializer.save(created_by=self.request.user)


class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = productserializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
