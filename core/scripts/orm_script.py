from core.models import Restaurant, Rating
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Fetch & return a single record, based on passing the value(s) in the model-field(s)
    rating = Rating.objects.get(rating=3)
    pprint(rating)

    pprint(connection.queries) # print out all the SQL queries