from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'birth_date', 'avatar', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'birth_date', 'avatar', 'bio')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)