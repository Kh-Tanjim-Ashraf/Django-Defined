from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail



class UserManager(BaseUserManager):

    def create_user(self, email, phone, password, **extra_fields):

        if not email:
            raise ValueError("Email is required!")
        
        if not phone:
            raise ValueError("Phone is required!")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            phone=phone, 
            **extra_fields
        )
        user.set_password(password)
        user.save()

        # TODO: Background Task: Send email to user about successful email creation
        send_mail(
            subject="Welcome!",
            message="Thank you for registering!",
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return user
    
    def create_superuser(self, email, phone, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email=email, phone=phone, password=password, **extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)

    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)

    phone = models.CharField(max_length=17)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.email