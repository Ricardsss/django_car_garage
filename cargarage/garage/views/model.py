from django.http import HttpResponse

from ..models import CarModel
from ..serializers import serialize_to_json


class ModelView:
    def models_list(request):
        query = CarModel.objects.all()
        models = serialize_to_json(query)
        return HttpResponse(models)
