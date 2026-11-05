from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = [
        "email",
        "username",
        "first_name",
        "mobile_number",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (
            "اطلاعات تکمیلی",
            {
                "fields": ("mobile_number", "age", "bio"),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "اطلاعات شناسایی",
            {
                "fields": (
                    "email",
                    "mobile_number",
                    "first_name",
                    "last_name",
                )
            },
        ),
    )
