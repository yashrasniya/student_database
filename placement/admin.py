from django.contrib import admin
from .models import PlacementCell, Recruiter, Cell, Achievement, Head , Subtitle

admin.site.register(Subtitle)
admin.site.register(Head)
admin.site.register(Achievement)
admin.site.register(Cell)
admin.site.register(PlacementCell)
admin.site.register(Recruiter)