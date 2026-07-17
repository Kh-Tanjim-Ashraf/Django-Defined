from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self, email, phone, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        
        if not phone:
            raise ValueError("Phone is required")

        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, phone, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        return self.create_user(email, phone, password, **kwargs)



class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=17)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.email