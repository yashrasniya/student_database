# admin.py in your Django app
from django.contrib import admin
from .models import Course, FooterLink, Mission, ActivityImage, Announcement

admin.site.register(Course)
admin.site.register(FooterLink)
admin.site.register(Mission)
admin.site.register(ActivityImage)
admin.site.register(Announcement)
