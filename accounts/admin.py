from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
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
    list_display = ("roll_number", "email", "first_name", "last_name", "is_staff")
    ordering = ("roll_number",)

