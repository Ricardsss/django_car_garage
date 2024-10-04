from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.core.validators import MinLengthValidator


# Create your models here.
class Make(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a car make (e.g. Nissan, Honda, Toyota etc.)",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("make-detail", args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="make_name_case_insensitive_unique",
                violation_error_message="Make already exists",
            )
        ]


class CarModel(models.Model):
    name = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("carmodel-detail", args=[str(self.id)])


class Car(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.RESTRICT)
    colour = models.CharField(max_length=200, help_text="Enter a colour for the car")
    year = models.CharField(max_length=4, validators=[MinLengthValidator(4)])
    VIN = models.CharField(
        max_length=17, validators=[MinLengthValidator(17)], unique=True
    )
    mileage = models.IntegerField()

    def __str__(self):
        return f"{self.colour} {self.car_model.make} {self.car_model} -- {self.year}"

    def get_absolute_url(self):
        return reverse("car-detail", args=[str(self.id)])


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    taken = models.DateField()
    due_back = models.DateField()

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.id} ({self.car})"
