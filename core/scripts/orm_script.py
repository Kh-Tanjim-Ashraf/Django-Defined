from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    restaurants = Restaurant.objects.all()[0:5] # Fetch the first 5 record from the DB.

    print(restaurants)

    print(connection.queries) # print out all the SQL queries