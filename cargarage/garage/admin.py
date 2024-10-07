from django.contrib import admin
from .models import Make, CarModel, Car, Rental


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


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ["car", "pick_up", "drop_off", "price"]
    list_filter = ["pick_up", "drop_off"]
    fieldsets = (
        (None, {"fields": ("car", "price")}),
        ("Availability", {"fields": ("pick_up", "drop_off")}),
    )
