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


def get_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)

        return JsonResponse(
            {
                "id": str(car.id),
                "car_model": car.car_model.name,
                "colour": car.colour,
                "year": car.year,
                "VIN": car.VIN,
                "mileage": car.mileage,
                "status": car.get_status_display(),
            },
            status=200,
        )

    except Car.DoesNotExist:
        return JsonResponse({"error": "Car not found"}, status=404)


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


def update_car(request, car_id):
    try:
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)

        data = json.loads(request.body)

        if "car_model" in data:
            car.car_model = validate_car_model(data.get("car_model"))

        if "colour" in data:
            car.colour = data.get("colour")

        if "year" in data:
            car.year = validate_year(data.get("year"))

        if "VIN" in data:
            car.VIN = validate_vin(data.get("VIN"))

        if "mileage" in data:
            car.mileage = validate_mileage(data.get("mileage"))

        if "status" in data:
            car.status = validate_status(data.get("status"), Car.RENTAL_STATUS)

        car.full_clean()
        car.save()

        return JsonResponse(
            {
                "id": str(car.id),
                "car_model": car.car_model.id,
                "colour": car.colour,
                "year": car.year,
                "VIN": car.VIN,
                "mileage": car.mileage,
                "status": car.get_status_display(),
            },
            status=200,
        )

    except ValidationError as ve:
        return JsonResponse({"error": str(ve)}, status=400)
    except IntegrityError as ie:
        return JsonResponse({"error": "VIN already exists"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)


def delete_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)

        car.delete()

        return JsonResponse({"message": "Car deleted successfully"}, status=200)

    except Car.DoesNotExist:
        return JsonResponse({"error": "Car not found"}, status=404)


class CarView:

    @csrf_exempt
    def cars(request):
        if request.method == "GET":
            return get_all_cars(request)
        elif request.method == "POST":
            return create_car(request)
        else:
            return JsonResponse(
                {"error": "Only GET or POST method allowed"}, status=405
            )

    @csrf_exempt
    def car(request, car_id):
        if request.method == "GET":
            return get_car_by_id(request, car_id)
        elif request.method == "PATCH":
            return update_car(request, car_id)
        elif request.method == "DELETE":
            return delete_car(request, car_id)
        else:
            return JsonResponse(
                {"error": "Only GET, PATCH or DELETE method allowed"}, status=405
            )
