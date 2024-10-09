from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from ..models import Car, Make, CarModel
from ..utils.validators import (
    validate_car_model,
    validate_year,
    validate_vin,
    validate_mileage,
    validate_status,
)
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

        required_fields = [
            "make_name",
            "model_name",
            "colour",
            "year",
            "VIN",
            "mileage",
        ]
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({"error": f"'{field}' is required."}, status=400)

        make_name = data["make_name"].strip()
        model_name = data["model_name"].strip()
        colour = data["colour"].strip()
        year = data["year"].strip()
        VIN = data["VIN"].strip()
        mileage = data["mileage"]

        if len(year) != 4:
            return JsonResponse(
                {"error": "The 'year' field must be 4 characters long."}, status=400
            )
        if len(VIN) != 17:
            return JsonResponse(
                {"error": "The 'VIN' field must be 17 characters long."}, status=400
            )

        make, created_make = Make.objects.get_or_create(name=make_name)

        car_model, created_model = CarModel.objects.get_or_create(
            name=model_name, make=make
        )

        car = Car(
            car_model=car_model, colour=colour, year=year, VIN=VIN, mileage=mileage
        )

        car.full_clean()
        car.save()

        return JsonResponse(
            {
                "car_id": car.id,
                "make_created": created_make,
                "model_created": created_model,
                "message": "Car created successfully.",
            },
            status=201,
        )

    except ValidationError as e:
        return JsonResponse({"error": e.message_dict}, status=400)

    except IntegrityError as e:
        return JsonResponse(
            {"error": "A car with this VIN already exists."}, status=400
        )

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def update_car(request, car_id):
    try:
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)

        data = json.loads(request.body)

        if "colour" in data:
            car.colour = data.get("colour")

        if "mileage" in data:
            car.mileage = validate_mileage(data.get("mileage"))

        if "status" in data:
            car.status = validate_status(data.get("status"), Car.RENTAL_STATUS)

        car.full_clean()
        car.save()

        return JsonResponse(
            {
                "id": str(car.id),
                "car_model": car.car_model.name,
                "car_make": car.car_model.make.name,
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
    if request.method == "DELETE":
        try:
            car = Car.objects.get(id=car_id)
            car_model = car.car_model
            make = car_model.make

            car.delete()

            remaining_cars_in_model = Car.objects.filter(car_model=car_model).exists()

            if not remaining_cars_in_model:
                car_model.delete()

                remaining_models_in_make = CarModel.objects.filter(make=make).exists()

                if not remaining_models_in_make:
                    make.delete()

            return JsonResponse({"message": "Car deleted successfully"}, status=200)

        except Car.DoesNotExist:
            return JsonResponse({"error": "Car not found."}, status=404)


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

    def get_cars_by_make(request, make_id):
        if request.method == "GET":
            try:
                make = Make.objects.get(id=make_id)

                cars = Car.objects.filter(car_model__make=make)

                cars_list = [
                    {
                        "id": car.id,
                        "model": car.car_model.name,
                        "make": car.car_model.make.name,
                        "colour": car.colour,
                        "year": car.year,
                        "VIN": car.VIN,
                        "mileage": car.mileage,
                        "status": car.get_status_display(),
                    }
                    for car in cars
                ]

                return JsonResponse(cars_list, safe=False, status=200)

            except Make.DoesNotExist:
                return JsonResponse({"error": "Make not found."}, status=404)

        return JsonResponse({"error": "Only GET method allowed"}, status=405)

    def get_cars_by_model(request, model_id):
        if request.method == "GET":
            try:
                car_model = CarModel.objects.get(id=model_id)

                cars = Car.objects.filter(car_model=car_model)

                cars_list = [
                    {
                        "id": car.id,
                        "model": car.car_model.name,
                        "make": car.car_model.make.name,
                        "colour": car.colour,
                        "year": car.year,
                        "VIN": car.VIN,
                        "mileage": car.mileage,
                        "status": car.get_status_display(),
                    }
                    for car in cars
                ]

                return JsonResponse(cars_list, safe=False, status=200)

            except CarModel.DoesNotExist:
                return JsonResponse({"error": "Car model not found."}, status=404)

        return JsonResponse({"error": "Only GET method allowed"}, status=405)
