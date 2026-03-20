from core.models import Restaurant
from django.utils import timezone

def run():
    restaurant = Restaurant()
    restaurant.name = 'My Italian Restaurant'
    restaurant.date_opened = timezone.now()
    restaurant.latitude = 51.2
    restaurant.longitude = 34.2
    restaurant.restaurant_type = Restaurant.RestaurantTypes.ITALIAN

    restaurant.save()