from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "kino-home"),
    path('staff', views.staff, name = "kino-staff"),
]