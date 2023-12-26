from django.db import models

from api.models import AuditedModel, MoneyField
from product.models import Product


class Order(AuditedModel):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(
        "auth.User", related_name="orders", on_delete=models.DO_NOTHING
    )
    shipping_address_line_1 = models.CharField(max_length=256)
    shipping_address_line_2 = models.CharField(max_length=256)
    shipping_country = models.CharField(max_length=128)
    shipping_state_province = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postal_code = models.CharField(max_length=32)

    billing_address_line_1 = models.CharField(max_length=256)
    billing_address_line_2 = models.CharField(max_length=256)
    billing_country = models.CharField(max_length=128)
    billing_state_province = models.CharField(max_length=128)
    billing_city = models.CharField(max_length=128)
    billing_postal_code = models.CharField(max_length=32)
    line_total = MoneyField()
    shipping_total = MoneyField()
    tax_total = MoneyField()
    dicounted_total = MoneyField()
    shipped = models.BooleanField()
    tracking_reference = models.CharField(max_length=128)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.id}{self.user.email}"
