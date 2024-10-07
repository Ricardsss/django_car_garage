from django.core import serializers


def serialize_to_json(query):
    return serializers.serialize("json", query)
