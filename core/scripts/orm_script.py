from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Create 3 sales record of the first restaurant
    Sale.objects.create(
        restaurant = Restaurant.objects.first(),
        income = 5.41,
        datetime = timezone.now()
    )

    Sale.objects.create(
        restaurant = Restaurant.objects.first(),
        income = 3.12,
        datetime = timezone.now()
    )

    Sale.objects.create(
        restaurant = Restaurant.objects.first(),
        income = 6.43,
        datetime = timezone.now()
    )

    pprint(connection.queries) # print out all the SQL queries