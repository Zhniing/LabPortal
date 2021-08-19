from django.contrib import admin
from .models import Author, Paper, Image

# Register your models here.

class AuthorManager(admin.ModelAdmin):
    list_display = ['name', 'English_name', 'email', 'grade']
    list_display_links = ['name']

admin.site.register(Author, AuthorManager)


class PaperManager(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'date']
    list_display_links = ['title']

admin.site.register(Paper, PaperManager)


# @admin.action(description='删除已选项')  # only available at version >= 3.2
def delete_selected(modeladmin, request, queryset):
    for item in queryset:
        item.delete()
delete_selected.short_description = '删除所选的 ' + Image._meta.verbose_name


class ImageManager(admin.ModelAdmin):
    list_display = ['id', 'image', 'paper', 'illustration', 'display_in_home']
    list_display_links = ['id']
    actions = [delete_selected]

admin.site.register(Image, ImageManager)
