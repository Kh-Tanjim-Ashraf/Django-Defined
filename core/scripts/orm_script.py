from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    restaurants = Restaurant.objects.all() # By default, it fetches total 21 records from the DB.
    
    print(restaurants)

    print(connection.queries) # print out all the SQL queries