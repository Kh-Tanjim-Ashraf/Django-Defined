from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    # Create a new record using the '.create()' method
    Restaurant.objects.create(
        name = "Pizza Shop",
        date_opened = timezone.now(),
        latitude = 51.3,
        longitude = 37.4,
        restaurant_type = Restaurant.RestaurantTypes.GREEK
    )

    print(connection.queries) # print out all the SQL queries