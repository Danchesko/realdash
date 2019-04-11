from django.contrib import admin

from .models import DashboardData

@admin.register(DashboardData)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ['servername', 'timestamp', 'memory_load', 'cpu_load']