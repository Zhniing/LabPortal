from django.contrib import admin
from .models import People, Paper

# Register your models here.

class PeopleManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'test']
    list_display_links = ['name']

admin.site.register(People, PeopleManager)


class PaperManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'authors']
    list_display_links = ['title']
    search_fields = ['title']
    # list_editable = ['authors']

admin.site.register(Paper, PaperManager)