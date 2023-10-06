from django.contrib import admin
from .models import Subject,OldPaper
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(OldPaper)
class OldPaperAdmin(admin.ModelAdmin):
    pass