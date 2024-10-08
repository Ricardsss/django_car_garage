from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Car, CarModel
from ..serializers import serialize_to_json


def get_cars(request):
    query = Car.objects.all()
    cars = serialize_to_json(query)
    return HttpResponse(json.loads(cars))


def add_car(request):
    try:
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        model = CarModel.objects.get(id=body["car_model"])
        body["car_model"] = model
        car = Car(**body)
        car.save()
        return HttpResponse(f"Car {car} has been added to the garage database")
    except Exception as e:
        return HttpResponse(e, status=422)


class CarView:

    @csrf_exempt
    def cars(request):
        if request.method == "GET":
            return get_cars(request)
        elif request.method == "POST":
            return add_car(request)
