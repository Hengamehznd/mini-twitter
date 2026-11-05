from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    mobile_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="شماره موبایل",
    )
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="سن")
    bio = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="بیوگرافی"
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "mobile_number", "first_name", "last_name"]

    def __str__(self):
        return f"{self.email}"
