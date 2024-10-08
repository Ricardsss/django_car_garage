from django.http import HttpResponse

from ..models import Rental
from ..serializers import serialize_to_json


class RentalView:
    def rentals_list(request):
        query = Rental.objects.all()
        rentals = serialize_to_json(query)
        return HttpResponse(rentals)
