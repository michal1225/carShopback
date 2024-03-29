from django.contrib import admin

from users.models import User

@admin.register(User)
class PartAdmin(admin.ModelAdmin):
    list_display = ["id", "username", 'first_name', 'last_name']