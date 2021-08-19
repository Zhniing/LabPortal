from django.contrib import admin
from .models import UploadImage

# Register your models here.

def delete_selected(modeladmin, request, queryset):
    for item in queryset:
        item.delete()
delete_selected.short_description = '删除所选的 ' + UploadImage._meta.verbose_name

class ImageManager(admin.ModelAdmin):
    list_display = ['id', 'upload', 'result_img']
    actions = [delete_selected]

admin.site.register(UploadImage, ImageManager)
