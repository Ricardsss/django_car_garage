from django.contrib import admin
from .models import Make, CarModel, Car


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name", "make"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["make", "car_model", "colour", "year", "mileage"]
    list_filter = ["car_model"]
