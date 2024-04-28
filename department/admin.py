# admin.py
from django.contrib import admin
from .models import Labs, Image, Working_communities, Department, NavBar


class LabsInline(admin.TabularInline):
    model = Department.department_labs_name.through
    extra = 0

class ImageInline(admin.TabularInline):
    model = Department.department_images.through
    extra = 0

class WorkingCommunitiesInline(admin.TabularInline):
    model = Working_communities
    extra= 1

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        LabsInline,
        ImageInline,
    ]

class Working_communitiesAdmin(admin.ModelAdmin):
    inlines= [
        WorkingCommunitiesInline,
    ]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Image)
admin.site.register(Labs)
admin.site.register(NavBar)
admin.site.register(Working_communities)