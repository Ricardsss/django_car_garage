from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from ..models import Car
from ..utils.validators import (
    validate_car_model,
    validate_year,
    validate_vin,
    validate_mileage,
    validate_status,
)
import uuid
import json


def get_all_cars(request):
    try:
        cars = Car.objects.all()

        cars_list = []
        for car in cars:
            cars_list.append(
                {
                    "id": str(car.id),
                    "model": car.model().name,
                    "make": car.make().name,
                    "colour": car.colour,
                    "year": car.year,
                    "VIN": car.VIN,
                    "mileage": car.mileage,
                    "status": car.get_status_display(),
                }
            )

        return JsonResponse(cars_list, safe=False, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def create_car(request):
    try:
        data = json.loads(request.body)

        car_model = validate_car_model(data.get("car_model"))
        colour = data.get("colour")
        year = validate_year(data.get("year"))
        VIN = validate_vin(data.get("VIN"))
        mileage = validate_mileage(data.get("mileage"))
        status = validate_status(data.get("status", "a"), Car.RENTAL_STATUS)

        if not colour:
            return JsonResponse({"error": "Colour is required"}, status=400)

        new_car = Car(
            id=uuid.uuid4(),
            car_model=car_model,
            colour=colour,
            year=year,
            VIN=VIN,
            mileage=mileage,
            status=status,
        )

        new_car.full_clean()
        new_car.save()

        return JsonResponse(
            {
                "id": str(new_car.id),
                "car_model": new_car.car_model.id,
                "colour": new_car.colour,
                "year": new_car.year,
                "VIN": new_car.VIN,
                "mileage": new_car.mileage,
                "status": new_car.get_status_display(),
            },
            status=201,
        )

    except ValidationError as ve:
        return JsonResponse({"error": str(ve)}, status=400)
    except IntegrityError as ie:
        return JsonResponse({"error": "VIN already exists"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)


class CarView:

    @csrf_exempt
    def cars(request):
        if request.method == "GET":
            return get_all_cars(request)
        elif request.method == "POST":
            return create_car(request)
