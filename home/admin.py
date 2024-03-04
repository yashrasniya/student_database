# admin.py in your Django app
from django.contrib import admin
from .models import Course,FooterLink

admin.site.register(Course)
admin.site.register(FooterLink)
