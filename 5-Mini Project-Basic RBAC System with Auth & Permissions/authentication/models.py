from django.db import models
from django.contrib.auth.models import User
from shared.models import TimestampMixins


class UserProfile(TimestampMixins):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
