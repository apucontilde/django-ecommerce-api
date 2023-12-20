from typing import Any
from django.db import models


class AuditedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class MoneyField(models.DecimalField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["decimal_places"] = 2
        kwargs["max_digits"] = 8
        super().__init__(*args, **kwargs)


class ProductCategory(AuditedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(AuditedModel):
    id = models.AutoField(primary_key=True)
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
