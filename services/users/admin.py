from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from services.users.models import User

admin.site.register(User, UserAdmin)
