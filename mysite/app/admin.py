from django.contrib import admin
from .models import Files
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

# Define an inline admin descriptor for User model


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Files)
