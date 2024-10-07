from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.cars_list, name="cars"),
    path("makes/", views.makes_list, name="makes"),
    path("models/", views.models_list, name="models"),
    path("rentals/", views.rentals_list, name="rentals"),
]
