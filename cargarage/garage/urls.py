from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.CarView.cars, name="cars"),
    path("cars/<uuid:car_id>/", views.CarView.car, name="car"),
    path(
        "cars_by_make/<str:make_id>/",
        views.CarView.get_cars_by_make,
        name="cars_by_make",
    ),
    path(
        "get_cars_by_model/<str:model_id>/",
        views.CarView.get_cars_by_model,
        name="get_cars_by_model",
    ),
    path("makes/", views.MakeView.makes, name="makes"),
    path("models/", views.ModelView.car_models, name="car_models"),
]
