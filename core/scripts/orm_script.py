from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Fetch a record & if not found, then create the record
    restaurant = Restaurant.objects.first()
    user = User.objects.first()
    rating, created = Rating.objects.get_or_create(
        user = user,
        restaurant = restaurant,
        rating = 4
    )
    print(rating)

    if created:
        # Send email, or execute other logic
        pass

    pprint(connection.queries) # print out all the SQL queries