from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("starter/", views.starter, name="starter-page"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("appointment/", views.appoint, name="appointment"),
    path("show/", views.show, name="show"),
    path('show/delete/<int:id>', views.delete),
    path('show/edit/<int:id>', views.edit),
    path('', views.register, name='register'),
    path('login/', views.login_user, name='login')
]