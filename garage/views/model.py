from django.http import JsonResponse


from ..models import CarModel


def get_all_car_models(request):
    car_models = CarModel.objects.select_related("make").all()

    car_model_list = [
        {"id": car_model.id, "name": car_model.name, "make": car_model.make.name}
        for car_model in car_models
    ]

    return JsonResponse(car_model_list, safe=False, status=200)


class ModelView:

    def car_models(request):
        if request.method == "GET":
            return get_all_car_models(request)
        else:
            return JsonResponse({"error": "Only GET method allowed"}, status=405)
