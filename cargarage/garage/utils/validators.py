from django.core.exceptions import ValidationError
from ..models import CarModel


def validate_car_model(car_model_name):
    try:
        car_model = CarModel.objects.get(name=car_model_name)
    except CarModel.DoesNotExist:
        raise ValidationError("Car model not found")
    return car_model


def validate_year(year):
    if not year or type(year) != str or len(year) != 4 or not year.isdigit():
        raise ValidationError("Year must be a 4 digit string")
    return year


def validate_vin(VIN):
    if not VIN or len(VIN) != 17:
        raise ValidationError("VIN must be exactly 17 characters long")
    return VIN


def validate_mileage(mileage):
    if not isinstance(mileage, int) or mileage < 0:
        raise ValidationError("Mileage must be a positive integer")
    return mileage


def validate_status(status, choices):
    if status not in dict(choices).keys():
        raise ValidationError("Invalid status value")
    return status
