# admin.py in your Django app
from django.contrib import admin
from .models import Mission, Vision, ActivityImage, Announcement, Course, FooterLink, MenuItem,\
    News, Event, Contact, TopHeaderLink,SliderImage
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name','parent','link','tree')

    def find_root_node(self,obj):
        if obj.parent:
            return self.find_root_node(obj.parent)+'/'+obj.name
        return obj.name

    def tree(self,obj):
        return self.find_root_node(obj)

admin.site.register(Mission)
admin.site.register(Vision)
admin.site.register(ActivityImage)
admin.site.register(Announcement)
admin.site.register(Course)
admin.site.register(FooterLink)

admin.site.register(News)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(TopHeaderLink)
admin.site.register(SliderImage)
