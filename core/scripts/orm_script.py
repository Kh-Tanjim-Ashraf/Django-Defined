from core.models import Restaurant, Rating
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Insert record into a table where foreign keys exists, for that, import the model instances first.
    user = User.objects.first() # Fetch the first user instance
    restaurant = Restaurant.objects.first() # Fetch the first user instance
    Rating.objects.create(
        user = user,
        restaurant = restaurant,
        rating = 3
    )
    pprint(Rating.objects.all())

    pprint(connection.queries) # print out all the SQL queries