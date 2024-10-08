from django.http import HttpResponse

from ..models import Make
from ..serializers import serialize_to_json


class MakeView:
    def makes_list(request):
        query = Make.objects.all()
        makes = serialize_to_json(query)
        return HttpResponse(makes)
