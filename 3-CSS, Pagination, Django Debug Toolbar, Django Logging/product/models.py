from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name