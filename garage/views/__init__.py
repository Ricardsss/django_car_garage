from django.http import HttpResponse
import json


from ..models import Car
from .car import CarView
from .make import MakeView
from .model import ModelView


def index(request):
    num_cars_available = Car.objects.filter(status__exact="a").count()
    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits

    details = {"numCarsAvailable": num_cars_available, "numVisits": num_visits}

    return HttpResponse(json.dumps(details))
