from django.contrib import admin
from .models import Feedback
# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass