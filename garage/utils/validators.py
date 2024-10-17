from django.core.exceptions import ValidationError
from ..models import CarModel


def validate_mileage(mileage):
    if not isinstance(mileage, int) or mileage < 0:
        raise ValidationError("Mileage must be a positive integer")
    return mileage


def validate_status(status, choices):
    if status not in dict(choices).keys():
        raise ValidationError("Invalid status value")
    return status
