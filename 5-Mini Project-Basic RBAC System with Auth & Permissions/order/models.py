from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from shared.models import TimestampMixins


class Order(TimestampMixins):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    ordered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.quantity * self.product.price
            
        super().save(*args, **kwargs)
