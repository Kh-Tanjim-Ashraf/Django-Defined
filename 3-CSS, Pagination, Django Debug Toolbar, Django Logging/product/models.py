from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(
        Category, 
        related_name='products', 
        on_delete=models.SET_NULL, 
        null=True,
        # db_index=True
    )

    def __str__(self):
        return self.name

"""
Table-splitting for DB optimization: Separating staic "Read-Heavy" & dynamic "Write-Heavy" tables to avoid "database lock contention".
"""

class Stock(models.Model):
    product_id = models.OneToOneField(
        Product, 
        related_name="stock", 
        on_delete=models.CASCADE, 
        # unique=True,
        # db_index=True
    ) # Using as both the PK & FK in this secondary table; Saves space in DB; **Shared Primary Key Pattern**
    quantity = models.PositiveIntegerField()