from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListCreateOrderAPIView.as_view(), name="get_post_orders"),
    path(
        "<int:pk>/",
        views.RetrieveUpdateDestroyOrderAPIView.as_view(),
        name="get_delete_update_order",
    ),
]
