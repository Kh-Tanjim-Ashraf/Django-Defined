from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin



@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ['id', 'email', 'phone', 'is_active', 'is_superuser']

    list_display_links = ['id', 'email']

    list_filter = ['is_active', 'is_superuser']

    search_fields = ['id', 'email', 'phone']

    ordering = ['id', 'email']

    add_fieldsets = (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "phone",
                "password1",
                "password2",
            ),
        }),