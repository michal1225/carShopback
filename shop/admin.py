from django.contrib import admin

from shop.models import Part


# Register your models here.
@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

