from django.contrib import admin
from .models import Category, Product, Stock, Review


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Review)