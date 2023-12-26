from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateProductAPIView.as_view(), name='get_post_products'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProductAPIView.as_view(), name='get_delete_update_product'),
]
