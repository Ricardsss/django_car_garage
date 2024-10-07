from django.http import HttpResponse
from datetime import datetime
import json

from .models import Car, Rental, Make, CarModel
from .serializers import serialize_to_json


def index(request):
    num_cars_available = Car.objects.filter(status__exact="a").count()
    active_rentals = Rental.objects.filter(drop_off__gte=datetime.today()).count()

    details = {
        "numCarsAvailable": num_cars_available,
        "activeRentals": active_rentals,
    }

    return HttpResponse(json.dumps(details))


def cars_list(request):
    query = Car.objects.all()
    cars = serialize_to_json(query)
    return HttpResponse(cars)


def makes_list(request):
    query = Make.objects.all()
    makes = serialize_to_json(query)
    return HttpResponse(makes)


def models_list(request):
    query = CarModel.objects.all()
    models = serialize_to_json(query)
    return HttpResponse(models)


def rentals_list(request):
    query = Rental.objects.all()
    rentals = serialize_to_json(query)
    return HttpResponse(rentals)
