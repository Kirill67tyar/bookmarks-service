from django.contrib import admin
from images.models import Image


@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):

    list_display = 'pk', 'title', 'slug', 'image', 'created',
    list_filter = 'created',