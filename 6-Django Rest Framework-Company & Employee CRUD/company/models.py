from django.db import models



class Company(models.Model):
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)