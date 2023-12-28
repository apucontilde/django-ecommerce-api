from typing import Any
from django.db import models


class AuditedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class MoneyField(models.DecimalField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["decimal_places"] = 2
        kwargs["max_digits"] = 8
        super().__init__(*args, **kwargs)
