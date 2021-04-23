from django.contrib import admin
from actions.models import Action


@admin.register(Action)
class ActionModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'verb', 'target', 'created',)
    list_filter = ('created',)
    search_fields = ('verb',)
