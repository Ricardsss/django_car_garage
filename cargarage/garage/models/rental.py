from django.db import models
import uuid

from .car import Car


class Rental(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pick_up = models.DateField()
    drop_off = models.DateField()

    class Meta:
        ordering = ["drop_off"]

    def __str__(self):
        return f"{self.id} ({self.car})"
