from django.contrib import admin
from .models import TrackingEntry


@admin.register(TrackingEntry)
class TrackingEntryAdmin(admin.ModelAdmin):
    list_display = ('task', 'created_at')
    search_fields = ('task__title', 'note')
