from django.db import models
from django.contrib.auth.models import User
from shared.models import TimestampMixins
from django.core.exceptions import ValidationError

class Product(TimestampMixins):
    # Build a unique composite field with name & price.
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)   # Later create an Admin Action for this field, thus an admin can toggle this field by selecting multiple products

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'price'],
                name='unique_product_name_price'
            )
        ]

    def __str__(self):
        return self.name

REVIEW_STATUS = [
    ('P', 'Pending'),
    ('A', 'Approved'),
    ('R', 'Rejected'),
    ('AO', 'Admin Operated')
]

# Each product has only one record in this table
class ProductCreateReview(TimestampMixins):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True, blank=True)
    proposed_name = models.CharField(max_length=100)
    proposed_price = models.DecimalField(max_digits=8, decimal_places=2)
    submitted_by = models.ForeignKey(User, verbose_name="Staff User", on_delete=models.SET_NULL, null=True, blank=True, related_name="product_creations_submitted")
    approved_by = models.ForeignKey(User, verbose_name="Admin User", on_delete=models.SET_NULL, null=True, blank=True, related_name="product_creations_approved")
    review_status = models.CharField(max_length=2, choices=REVIEW_STATUS, default='P')

    def __str__(self):
        return self.proposed_name


# Multiple updates can be proposed by multiple staff user in different timeline
class ProductUpdateReview(TimestampMixins):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='update_logs')
    proposed_name = models.CharField(max_length=100, null=True, blank=True)
    proposed_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    submitted_by = models.ForeignKey(User, verbose_name="Staff User", on_delete=models.SET_NULL, null=True, blank=True, related_name="product_modifications_submitted")
    approved_by = models.ForeignKey(User, verbose_name="Admin User", on_delete=models.SET_NULL, null=True, blank=True, related_name="product_modifications_approved")
    review_status = models.CharField(max_length=2, choices=REVIEW_STATUS, default='P')

    def __str__(self):
        return self.product.name