from django.urls import reverse
from product.models import Product, ProductCategory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ProductApiTest(APITestCase):
    def setUp(self):
        user = User.objects.create_user("username", "Pas$w0rd")

        self.category = ProductCategory.objects.create(name="Cookware", created_by=user)
        self.product = Product.objects.create(
            short_name="Fancy Teacup",
            long_name="A very Fancy and Shinny Teacup",
            sku="AAA111",
            price=12.3,
            stock=3,
            physical_height=0,
            physical_lenght=0,
            physical_width=0,
            created_by=user,
        )
        self.product.categories.set([self.category])
        self.client.force_authenticate(user)
        self.url = reverse("get_post_products")

    def test_get_products_no_filter(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_short_name(self):
        response = self.client.get(
            self.url, data={"short_name": self.product.short_name}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_short_name_sad(self):
        response = self.client.get(
            self.url, data={"short_name": "this product doesnt exist"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_get_products_filter_by_long_name(self):
        response = self.client.get(self.url, data={"long_name": "Fancy"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_long_name_sad(self):
        response = self.client.get(
            self.url, data={"long_name": "this product doesnt exist"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_get_products_filter_by_category_name(self):
        response = self.client.get(
            self.url, data={"category": self.category.name}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_category_name_sad(self):
        response = self.client.get(
            self.url, data={"category": "This Category Doesnt Exist"}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_get_products_filter_by_price_gt_happy(self):
        response = self.client.get(self.url, data={"price_gt": 10}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_price_lte_happy(self):
        response = self.client.get(self.url, data={"price_lte": 14}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_price_lte_sad(self):
        response = self.client.get(self.url, data={"price_lte": 0}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)

    def test_get_products_filter_by_stock_gt_happy(self):
        response = self.client.get(self.url, data={"stock_gt": 1}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_stock_lte_happy(self):
        response = self.client.get(self.url, data={"stock_lte": 3}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_get_products_filter_by_stock_lte_sad(self):
        response = self.client.get(self.url, data={"stock_lte": 0}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)
