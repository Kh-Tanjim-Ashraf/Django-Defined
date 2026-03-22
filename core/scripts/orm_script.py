from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Fetch all the sale-records of a specific restaurant using that specific restaurant instance.
    restaurant = Restaurant.objects.first()
    sales = restaurant.sales.all()
    print(sales)

    pprint(connection.queries) # print out all the SQL queries