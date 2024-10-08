from datetime import datetime
from django.http import HttpResponse
import json


from ..models import Car, Rental
from .car import CarView
from .make import MakeView
from .model import ModelView
from .rental import RentalView


def index(request):
    num_cars_available = Car.objects.filter(status__exact="a").count()
    active_rentals = Rental.objects.filter(drop_off__gte=datetime.today()).count()

    details = {
        "numCarsAvailable": num_cars_available,
        "activeRentals": active_rentals,
    }

    return HttpResponse(json.dumps(details))
