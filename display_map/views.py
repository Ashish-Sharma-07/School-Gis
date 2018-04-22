from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from display_map.models import MahaSchoolCentroidRti1314
import json


def index(request):
    schools = MahaSchoolCentroidRti1314.objects.all()[:20]
    points = serialize('geojson', schools,
                       geometry_field='geom', )
    points = json.loads(points)
    points.pop('crs', None)
    points = json.dumps(points)
    return HttpResponse(render(request, 'display_map/index.html', {'points': points}))
