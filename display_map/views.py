from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from display_map.models import MahaSchoolCentroidRti1314
import json 

# Create your views here.
def index(request):
	#with open("display_map/static/data/maha_school_centroid_rti_13_14_0.json", "w") as out:
	schools = MahaSchoolCentroidRti1314.objects.all()
	points = serialize('geojson',schools,
	geometry_field='geom',)
	#fields=('fid','district_n','taluka_nam','census_201','area_name','disname','blockname','villagenam','udisecode',
	#'schoolname','schcategor','pincode','lowclass','highclass','preprimary','preprima_1','medium'))
	points = json.loads(points)
	points.pop('crs',None)
	points = json.dumps(points)
        

	return HttpResponse(render(request,'display_map/index.html',{'points':points}))
