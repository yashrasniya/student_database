from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Superuser,CR
from .utils import actions
from django.db.models import Q

# Register your models here.

@admin.register(User)
class UserAdmin(actions,UserAdmin):
    fieldsets = (
        (None, {"fields": ("roll_number", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",'gender','Mother_name','Father_name','profile','dob')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_cr",
                    # "user_permissions",
                ),
            })
            ,
        (("address"),
            {
                "fields": (
                    "country",
                    "state",
                    "city",
                    "landmark",
                    "pincode",
                    "address",
                ),
            }),(
             ("Contect"),
        {
            "fields": (
                "mobile_number",
                "parent_mobile_number",

            ),
        }),
        (
            ("other information"),
            {
                "fields": (
                    "adhar_number",
                    "marksheet_10",
                    "marksheet_12",

                ),
            }),
            (
                ("collage"),
                {
                    'fields':(
                        'branch',
                        'batch',
                    ),
                },

        ),
        # (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("roll_number", "password1", "password2"),
            },
        ),
    )
    list_filter=['branch','batch','is_staff','gender',]
    search_fields = [
        'roll_number',
        'Father_name',
        'Mother_name',
        'dob',
        'country',
        'state',
        'city',
        'landmark',
        'address',
        'pincode',
        'mobile_number',
        'parent_mobile_number',
        'adhar_number',
    ]
    list_display = ("roll_number", "name","branch","batch","Father_name")
    ordering = ("roll_number",)
    def get_queryset(self, request):
        return self.model.objects.filter(is_superuser=False,is_staff=False)

@admin.register(Superuser)
class admin_users(UserAdmin):
    fieldsets = (
        (None, {"fields": ("roll_number", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email",'gender','Mother_name','Father_name','profile','dob')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_cr",
                    # "is_partner",
                    "user_permissions",
                    "groups",
                ),
            },
        ),
        # (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display=("roll_number", "name","is_superuser","is_staff",'email')
    def get_queryset(self, request):
        return self.model.objects.filter(Q(is_superuser=True)| Q(is_staff=True))


@admin.register(CR)
class admin_users(UserAdmin):

    def get_queryset(self, request):
        return self.model.objects.filter(is_cr=True)


