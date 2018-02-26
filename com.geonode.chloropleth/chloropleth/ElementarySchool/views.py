# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,HttpResponse,Http404,HttpResponseRedirect,render
from .models import district_boundaries,taluka_boundaries,state_maharashtra,SchoolInfo
from django.core.serializers import serialize
from colour import Color
from django.db.models import Count,Sum
from .forms import AttributeForm
import json


def get_base_map(request):
    district = state_maharashtra.objects.all().order_by('district')
    # serialize the data
    district_serialize = serialize('geojson', district,
                                   geometry_field='geom',
                                   fields=('district',))
    dist_json = json.loads(district_serialize)
    # remove crs field
    dist_json.pop('crs', None)
    district = json.dumps(dist_json)

    return render_to_response('chloropleth/maps.html', {'district': district,'name':"Base Map"})


# Create your views here.
def get_map(request,feature):
    district = state_maharashtra.objects.all().order_by('district')

    #serialize the data
    district_serialize = serialize('geojson', district,
          geometry_field='geom',
          fields=('district',))

    #create a dictionary
    max_v = 0
    min_v = 1000
    dist_json = json.loads(district_serialize)
    # remove crs field
    dist_json.pop('crs',None)
    for i in range(len(district)):
        d_name = dist_json['features'][i]['properties']['district']
        features = SchoolInfo.objects.values(str(feature)).filter(distname__iexact = d_name).aggregate(Sum(str(feature)))

        if(min_v > features[str(feature)+'__sum']):
            min_v = features[str(feature)+'__sum']
        if (max_v < features[str(feature) + '__sum']):
            max_v = features[str(feature) + '__sum']

        rag = max_v - min_v

        dist_json['features'][i]['properties']['feature_val'] = features[str(feature)+'__sum']
    district = json.dumps(dist_json)

    grade = [round(float(i*rag)/100,2) for i in range(0,110,20)]
    color_list = list(str(i) for i in Color('yellow').range_to(Color('red'), len(grade)))
    return render_to_response('chloropleth/maps.html',{'district':district,'Name':str(feature),'range':rag,
                                                       'grade':grade,'color':color_list})

def Grade(request):

    try:
        from colour import Color
        dark_blue = Color('darkblue')
        light_blue = Color('lightblue')
        color_list = list(str(i) for i in light_blue.range_to(dark_blue,5))

        #Get districts shape
        district = state_maharashtra.objects.all().order_by('district')

        # serialize the data
        district_serialize = serialize('geojson', district,
                                       geometry_field='geom',
                                       fields=('district',))
        # create a dictionary
        dist_json = json.loads(district_serialize)

        # remove crs field
        dist_json.pop('crs', None)

        max_v = 0
        min_v = 1000
        weights = ['', 0, 0, 0, 1, 0]

        for i in range(len(district)):
            d_name = dist_json['features'][i]['properties']['district']
            water_info = SchoolInfo.objects.values('water').annotate(Count('water')).filter(distname__iexact=d_name).order_by('water')

            weighted_values = list()
            for x in water_info:
                if (x.get('water')) is not None:
                    if (int(x.get('water')) == 9):
                        continue
                weighted_values.append(round(weights[int(x.get('water'))] * x.get('water__count'),3))
                temp = round(sum(weighted_values) / len(weighted_values),2)
                if (temp>max_v):
                    max_v = temp
                if (temp<min_v):
                    min_v = temp
            dist_json['features'][i]['properties']['water'] = temp
        district = json.dumps(dist_json)
        range_value = max_v - min_v
        return render_to_response('chloropleth/water.html', {'district': district, 'Name': "Water Quality",'range':range_value,'color':color_list })

    except IndexError ,e:
        raise Http404("Nope")


def get_features(request):
    form = AttributeForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AttributeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print form.cleaned_data
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AttributeForm()

    return render(request,'chloropleth/form.html',{'form':form})