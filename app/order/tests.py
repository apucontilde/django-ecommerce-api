from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class OrdersApiTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(user)
        self.url = reverse("get_post_orders")

    def test_create_order(self):
        pass

    def test_update_order_status(self):
        pass

    def test_get_orders_of_user(self):
        pass
