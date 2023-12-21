from typing import Any
from django.db import models

from api.models import AuditedModel, MoneyField


class ProductCategory(AuditedModel):
    name = models.CharField(max_length=36)

    class Meta:
        ordering = ["name"]
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Product(AuditedModel):
    short_name = models.CharField(max_length=36)
    long_name = models.CharField(max_length=100)
    sku = models.CharField(max_length=36)
    price = MoneyField()
    stock = models.IntegerField()
    thumbnail = models.CharField(max_length=256)
    # physical dimentions
    physical_width = models.FloatField()
    physical_lenght = models.FloatField()
    physical_height = models.FloatField()
    categories = models.ManyToManyField(ProductCategory, related_name="products")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.sku}{self.short_name}"
