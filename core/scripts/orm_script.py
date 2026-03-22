from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    # Query & fetch the last record using the '.last()' method
    restaurant = Restaurant.objects.last()
    print(restaurant)

    print(connection.queries) # print out all the SQL queries