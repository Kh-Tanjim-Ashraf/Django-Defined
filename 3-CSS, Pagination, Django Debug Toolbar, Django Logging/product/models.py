from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TimestampMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimestampMixins):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Many-To-Many Relationship
class Product(TimestampMixins):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name

"""
Table-splitting for DB optimization: Separating static "Read-Heavy" & dynamic "Write-Heavy" tables to avoid "database lock contention".
"""

# One-To-One Relationship
class Stock(TimestampMixins):
    product = models.OneToOneField(
        Product, 
        related_name="stock", 
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

# One-To-Many Relationship
class Review(TimestampMixins):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.name