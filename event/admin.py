from django.contrib import admin
from .models import Event

# Register your models here.

class EventInline(admin.TabularInline):
    model = Event
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines= [
        EventInline,
    ]