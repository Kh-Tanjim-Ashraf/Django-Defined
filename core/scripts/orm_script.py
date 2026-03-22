from core.models import Restaurant, Rating
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Fetch & return a queryset (list), based on passing the value(s) in model-field(s)
    rating = Rating.objects.filter(rating=3)
    pprint(rating)

    pprint(connection.queries) # print out all the SQL queries