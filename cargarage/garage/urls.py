from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.CarView.cars, name="cars"),
    path("cars/<uuid:car_id>/", views.CarView.car, name="car"),
    path("makes/", views.MakeView.makes_list, name="makes"),
    path("models/", views.ModelView.models_list, name="models"),
]
