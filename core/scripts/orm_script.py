from core.models import Restaurant, Rating
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():
    # Fetch all the ratings of a specific restaurant; using the '{main_model}.{model}_set.all()' manager
    restaurant = Restaurant.objects.first()
    ratings = restaurant.ratings.all()
    pprint(ratings)

    pprint(connection.queries) # print out all the SQL queries