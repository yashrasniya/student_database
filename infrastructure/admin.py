# admin.py

from django.contrib import admin
from .models import Infrastructure

class InfrastructureInline(admin.TabularInline):
    model = Infrastructure
    extra = 0

@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
