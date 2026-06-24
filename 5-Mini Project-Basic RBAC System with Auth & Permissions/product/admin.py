from django.contrib import admin, messages
from product.models import Product, ProductCreateReview, ProductUpdateReview
from product.services.productApprovalService import ProductApprovalService
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']

    def check_duplicate(self, request, obj):
        # Check if an update review w/ same product FK & review_status='Pending' exists
        if ProductUpdateReview.objects.filter(
            product=obj,
            review_status='P'
        ).exists():
            if request.user.is_superuser:
                ProductUpdateReview.objects.filter(product=obj, review_status='P').update(
                    proposed_name = obj.name,
                    proposed_price = obj.price,
                    is_active = obj.is_active,
                    approved_by = request.user,
                    review_status = 'AO'
                )
            else:
                messages.error(
                    request,
                    f"{obj}: An update is already pending in 'ProductUpdateReview'"
                )
                
            return True

    def save_model(self, request, obj, form, change):

        if change:
            # Record update logic
            if request.user.is_superuser:
                # Admin update; Check in the 'ProductUpdateReview' table, if any record is 'Pending' with similar product FK value, then change it's review_status='Admin Operated' & make the 'is_active' field same as the record in 'Product' table. Fields: proposed_name, proposed_price,is_active, approved_by, review_status

                # If duplicate found; change the record inside 'ProductUpdateReview' & directly reflect the change in 'Product' table made by the admin.
                if self.check_duplicate(request, obj):
                    return super().save_model(request, obj, form, change)
                
                # If no duplicate exists; create a record in 'ProductUpdateReview' & then directly reflect the change in 'Product' table made by the admin using the final `super().save_model()` model of this method.
                ProductUpdateReview.objects.create(
                    product = obj,
                    proposed_name = obj.name,
                    proposed_price = obj.price,
                    is_active = obj.is_active,
                    approved_by = request.user,
                    review_status = 'AO'
                )

            else:
                # Staff Update; Similarly check if record exists in 'ProductUpdateReview' table. If exists, prevent the staff to create another record in that table, otherwise, simply create a record with review_status='Pending' there, without letting that staff to directly udpate the record in 'Product' table.

                if self.check_duplicate(request, obj):
                    return # Prevent staff to update the product detail directly
                
                # If no duplicate exists, create a record inside 'ProductUpdateReview', which will be later reviewed by an admin
                ProductUpdateReview.objects.create(
                    product=obj,
                    proposed_name=obj.name,
                    proposed_price=obj.price,
                    is_active=obj.is_active,
                    submitted_by=request.user,
                    review_status='P'
                )

                return # Prevent staff to update the product detail directly
                    
        else:
            # Record create logic

            # Check if a record w/ same name & price. Only a single record will exists by chance.
            if ProductCreateReview.objects.filter(
                proposed_name=obj.name,
                proposed_price=obj.price,
            ).exists():
                # If though it exists, then change it's status to 'Cancelled' & attach the product w/ the record as FK
                pcr_obj = ProductCreateReview.objects.get(
                    proposed_name=obj.name,
                    proposed_price=obj.price,
                )

                # Both queries must complete, otherwise rollback
                # Queries: (1) Create 'Product' (2) Update 'ProductCreateReview'
                with transaction.atomic():
                    # Create the `Product` first, in order to define the record as FK in `ProductCreateReview`
                    super().save_model(request, obj, form, change)
                    
                    pcr_obj.product = obj
                    pcr_obj.approved_by = request.user
                    pcr_obj.review_status = 'AO'
                    pcr_obj.save(update_fields=[
                        'product',
                        'approved_by',
                        'review_status'
                    ])
                    
                return # Stop to execute `super().save()` method again
                
            else:
                # If no create-review-record found in 'ProductCreateReview' table with same name & price, then create a record in that table.

                with transaction.atomic():
                    # Create the `Product` first, in order to define the record as FK in `ProductCreateReview`
                    super().save_model(request, obj, form, change)

                    ProductCreateReview.objects.create(
                        product=obj,
                        proposed_name=obj.name,
                        proposed_price=obj.price,
                        approved_by=request.user,
                        review_status='AO'
                    )

                    return
        
        return super().save_model(request, obj, form, change)


@admin.register(ProductCreateReview)
class ProductCreateReviewAdmin(admin.ModelAdmin):
    list_display = ['proposed_name', 'proposed_price', 'submitted_by', 'approved_by', 'review_status', 'product']
    readonly_fields = ['submitted_by', 'approved_by', 'product']   # No one is allowed to change the user detail, handled automatically by the system

    def get_readonly_fields(self, request, obj=None):
        # Fetch the baseline readonly fields
        readonly_fields = list(super().get_readonly_fields(request, obj))

        if request.user.is_superuser:
            # Superuser; Only allowed to change the review status in edit page

            # Note: If the Admin creates a record in 'ProductCreateReview', the review status should be "Approved" conditionally. Thus it's unnecessary to provide the admin with the option to change the review status while creating a record.

            if obj is None:
                # Record Creation Page; Make "review_status" field readonly
                readonly_fields.extend(['review_status'])

        else:
            # Staff user
            readonly_fields.extend(['review_status'])
        
        return readonly_fields

    def check_duplicate(self, request, obj):
        if ProductCreateReview.objects.filter(
            proposed_name=obj.proposed_name,
            proposed_price=obj.proposed_price
        ).exists():
            messages.error(
                request,
                "Duplicate found. Record was not saved."
            )
            return True

    def save_model(self, request, obj, form, change):
        if change:
            # Record Update Logic
            obj.approved_by = request.user

            # Only create record in 'Product' table if approved by Admin
            if obj.review_status == 'A' and not obj.product:
                ProductApprovalService.approve(review_obj=obj)

        else:
            # Record Create Logic: (Staff, Admin) POVs

            # Check duplicate, if found, prevent record creation
            if self.check_duplicate(request, obj):
                return

            if request.user.is_superuser:
                # Created by Admin
                obj.approved_by = request.user

                # Automatically make the review status as "Approved"
                # Admin doesn't have the option to change the review status while creating a new review record
                obj.review_status = 'A'

                # Create a record in "Product" table automatically;
                ProductApprovalService.approve(review_obj=obj)
                    
            else:
                # Created by Staff
                obj.submitted_by = request.user

        return super().save_model(request, obj, form, change)



@admin.register(ProductUpdateReview)
class ProductUpdateReviewAdmin(admin.ModelAdmin):
    list_display = ['proposed_name', 'proposed_price', 'is_active', 'submitted_by', 'approved_by', 'review_status', 'product']
    readonly_fields = ['submitted_by', 'approved_by']

    def get_readonly_fields(self, request, obj=None):
        # Fetch the baseline readonly fields
        readonly_fields = list(super().get_readonly_fields(request, obj))

        if request.user.is_superuser:
            # Superuser; Only allowed to change the review status in edit page

            # Note: If the Admin creates a record in 'ProductCreateReview', the review status should be "Approved" conditionally. Thus it's unnecessary to provide the admin with the option to change the review status while creating a record.

            if obj is None:
                # Record Creation Page; Make "review_status" field readonly
                readonly_fields.extend(['review_status'])

        else:
            # Staff user
            readonly_fields.extend(['review_status'])
        
        return readonly_fields

    def check_duplicate(self, request, obj):
        # Check if an update review w/ same product FK & review_status='Pending' exists
        if ProductUpdateReview.objects.filter(
            product=obj.product,
            review_status='P'
        ).exists():
            messages.error(
                request,
                "Duplicate found. Record was not saved."
            )
            return True

    def save_model(self, request, obj, form, change):
        if change:
            # Record Update Logic
            obj.approved_by = request.user

            # Only update record in 'Product' table if approved by Admin
            if obj.review_status == 'A' and obj.product:
                ProductApprovalService.approve(review_obj=obj, product=obj.product)

        else:
            # Record Create Logic

            # Check duplicate, if found, prevent record creation
            if self.check_duplicate(request, obj):
                return
            
            if request.user.is_superuser and obj.product:
                # Admin User
                obj.approved_by = request.user
                obj.review_status = 'A'

                ProductApprovalService.approve(review_obj=obj, product=obj.product)
            else:
                # Staff User
                obj.submitted_by = request.user

        return super().save_model(request, obj, form, change)