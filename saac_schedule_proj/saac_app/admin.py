from django.contrib import admin
from .models import Event, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class RegisteredEventInline(admin.TabularInline):
    model = Event.registered_users.through


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

    inlines = [RegisteredEventInline]


class EventAdmin(admin.ModelAdmin):
    # You can specify fields that will be shown in the admin form
    list_display = ('title', 'start', 'end', 'location', 'get_registered_users')
    search_fields = ['title', 'description']

    # Add a method to display the registered users in the list view
    def get_registered_users(self, obj):
        return ", ".join([str(user) for user in obj.registered_users.all()])

    get_registered_users.short_description = 'Registered Users'

    # You can also customize the form for adding/editing the event to show the ManyToMany field
    filter_horizontal = ('registered_users',)  # This adds a two-column interface for the ManyToMany relationship


# Register the custom admin interface
admin.site.register(Event, EventAdmin)
# admin.site.register(Event)
admin.site.register(CustomUser, CustomUserAdmin)
