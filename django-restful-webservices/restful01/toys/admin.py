from django.contrib import admin

# Register your models here.
from .models import Toy


class Toys(admin.ModelAdmin):
    list_display = ('name', 'description', 'toy_category', 'release_date', 'created', 'was_included_in_home')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Toy, Toys)
