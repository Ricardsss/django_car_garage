from django.http import HttpResponse
import json


from ..models import Car
from .car import CarView
from .make import MakeView
from .model import ModelView


def index(request):
    num_cars_available = Car.objects.filter(status__exact="a").count()

    details = {"numCarsAvailable": num_cars_available}

    return HttpResponse(json.dumps(details))
