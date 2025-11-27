from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("starter/", views.starter, name="starter-page"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("appointment/", views.appoint, name="appointment")
]