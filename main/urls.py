from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name = "index"),
    path("register", views.register_request, name = "register"),
    path("login", views.login_request, name = "login"),
    path("logout", views.logout_request, name = "logout"),
    path("submit", views.submit_request, name = "submit"),
    path("add", views.add_request, name = "add"),
    path("newsources", views.new_subjects_or_units_request, name = "newunits"),
]