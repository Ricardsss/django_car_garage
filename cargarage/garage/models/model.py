from django.db import models
from django.urls import reverse


from .make import Make


class CarModel(models.Model):
    name = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("carmodel-detail", args=[str(self.id)])
