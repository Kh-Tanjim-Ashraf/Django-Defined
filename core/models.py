from django.db import models
from django.contrib.auth.models import User

# Models: Restaurant, Rating, Sale

class Restaurant(models.Model):
    class RestaurantTypes(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GK', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fastfood'
        OTHER = 'OT', 'Other'
    
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=RestaurantTypes.choices)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.restaurant} -- {self.user} -- {self.rating}'


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()

