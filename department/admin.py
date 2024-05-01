# admin.py
from django.contrib import admin
from .models import Image, Working_communities, Department, NavBar, Lab, Practical


class ImageInline(admin.TabularInline):
    model = Department.department_images.through
    extra = 1


class WorkingCommunitiesInline(admin.TabularInline):
    model = Working_communities
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    filter_horizontal = [
        'department_subjects_name',
        'department_labs_name',
        'department_images',
        'department_subjects_name',
        'deparment_faculty',
    ]
    inlines = [

        ImageInline,
    ]


class Working_communitiesAdmin(admin.ModelAdmin):
    inlines = [
        WorkingCommunitiesInline,
    ]


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('practical',)


@admin.register(Practical)
class PracticalAdmin(admin.ModelAdmin):
    list_display = ('topic',)


admin.site.register(Image)
admin.site.register(NavBar)
admin.site.register(Working_communities)
