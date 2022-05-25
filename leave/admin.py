from django.contrib import admin

from leave import serializers
from . import models
# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
    list_display = ['user', 'requested_at', 'start_date', 'end_date', 'status']
    ordering = ['requested_at']
    # search_fields = ['user__name__istartswith', 'last_name__istartswith']

admin.site.register(models.Leave, LeaveAdmin)


