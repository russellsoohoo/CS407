from django.contrib import admin
from .models import Event
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


admin.site.register(Event)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'sport', 'grad_year', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'sport', 'grad_year']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'sport', 'grad_year')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'sport', 'grad_year', 'is_active',
                'is_staff')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
