from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile_number",
            "age",
            "bio",
        )


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "mobile_number",
            "age",
            "bio",
        )


# class LoginForm(AuthenticationForm):
#     username = forms.EmailField(
#         label="ایمیل",
#         widget=forms.EmailInput(
#             attrs={"placeholder": "ایمیل خود را وارد کنید", "class": "form-control"},
#         ),
#     )

#     password = forms.CharField(
#         label="رمز عبور",
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "رمز عبور", "class": "form-control"},
#         ),
#     )
