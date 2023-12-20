from typing import Any
from django.db import models

class AuditedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class Meta:
        abstract = True

class MoneyField(models.DecimalField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["decimal_places"] = 2
        kwargs["max_digits"] = 8
        super().__init__(*args, **kwargs)
    

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
    categories = models.ForeignKey('ProductCategory', related_name='products', on_delete=models.DO_NOTHING)
    class Meta:
        ordering = ['-id']

class ProductCategory(AuditedModel):
    name = models.CharField(max_length=36)

