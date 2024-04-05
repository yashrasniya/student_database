# admin.py
from django.contrib import admin
from .models import *
from old_paper.models import Subject

class SubjectInline(admin.TabularInline):
    model = Department.department_subjects_name.through
    extra = 1

class LabsInline(admin.TabularInline):
    model = Department.department_labs_name.through
    extra = 1

class ImageInline(admin.TabularInline):
    model = Department.department_images.through
    extra = 1

class WorkingCommunitiesInline(admin.TabularInline):
    model = Working_communities
    extra = 1

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [
        SubjectInline,
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
admin.site.register(Working_communities, Working_communitiesAdmin)