from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    # Count the total number of records using the '.count()' method
    print(Restaurant.objects.count())

    print(connection.queries) # print out all the SQL queries