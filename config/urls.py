from django.contrib import admin
from django.urls import path, include
from users import views as ac_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("twit.urls")),
    path("register/", ac_views.register_view, name="register"),
    path("login/", ac_views.login_view, name="login"),
    path("logout/", ac_views.logout_view, name="logout"),
]
