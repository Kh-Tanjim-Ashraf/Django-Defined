from django.db import transaction
from django.utils import timezone
from product.models import Product


class ProductApprovalService:

    @staticmethod
    @transaction.atomic
    def approve(review_obj, product=None):
        if product:
            # Logic for 'ProductUpdateReview' table
            product.name = review_obj.proposed_name
            product.price = review_obj.proposed_price
            product.is_active = review_obj.is_active
            
            product.save()

            return product  # Optional
            
        else:
            # Logic for 'ProductCreateReview' table
            
            # Create record in 'Product' table
            product, created = Product.objects.update_or_create(
                name = review_obj.proposed_name,
                price = review_obj.proposed_price,
                defaults={
                    "name": review_obj.proposed_name,
                    "price": review_obj.proposed_price
                }
            )

            # Define the product record to the 'ProductCreateReview' table
            review_obj.product = product

            return product  # Optional
