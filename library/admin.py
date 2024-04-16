# admin.py

from django.contrib import admin
from .models import Book,Staff,Announcement


admin.site.register(Announcement)
admin.site.register(Book)
admin.site.register(Staff)