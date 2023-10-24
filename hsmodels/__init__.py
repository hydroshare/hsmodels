from rdflib.serializer import Serializer
from rdflib.plugin import register


register(
    'json-ld-pretty', Serializer,
    'hsmodels.serializers', 'PrettyJsonLDSerializer')