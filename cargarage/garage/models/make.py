from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


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
