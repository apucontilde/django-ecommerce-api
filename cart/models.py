from django.db import models

from api.models import AuditedModel
from product.models import Product


class Cart(AuditedModel):
    products = models.ManyToManyField(Product)
