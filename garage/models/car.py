from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
import uuid

from .model import CarModel


class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car_model = models.ForeignKey(CarModel, on_delete=models.RESTRICT)
    colour = models.CharField(max_length=200, help_text="Enter a colour for the car")
    year = models.CharField(max_length=4, validators=[MinLengthValidator(4)])
    VIN = models.CharField(
        max_length=17, validators=[MinLengthValidator(17)], unique=True
    )
    mileage = models.IntegerField()

    RENTAL_STATUS = (("a", "Available"), ("u", "Unavailable"), ("m", "Maintenance"))

    status = models.CharField(
        max_length=1, choices=RENTAL_STATUS, blank=True, default="a"
    )

    def model(self):
        return self.car_model

    def make(self):
        return self.car_model.make

    def __str__(self):
        return f"{self.colour} {self.make()} {self.model()} -- {self.year}"

    def get_absolute_url(self):
        return reverse("car-detail", args=[str(self.id)])
