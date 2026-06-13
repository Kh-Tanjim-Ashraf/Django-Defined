from django.db import models


class TimestampMixins(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Category(TimestampMixins):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(TimestampMixins):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ManyToManyField(
        Category, 
        related_name='products', 
    )

    def __str__(self):
        return self.name

"""
Table-splitting for DB optimization: Separating staic "Read-Heavy" & dynamic "Write-Heavy" tables to avoid "database lock contention".
"""

class Stock(TimestampMixins):
    product_id = models.OneToOneField(
        Product, 
        related_name="stock", 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product_id.name
