# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import Http404, render,HttpResponse
from django.core.serializers import serialize
from colour import Color
from django.apps.registry import apps
blockSummary = apps.get_model('state_level','BlockSummary')
districtSummary = apps.get_model('state_level','DistrictSummary')
import json
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.views.decorators.csrf import csrf_exempt
from math import floor

features = {
    'water':[('water_1','hand pump'),('water_2','well'),('water_3','tap water'),('water_4','other'),('water_5','none'),],

    'sanitation':[
        ('toiletwater_g', "Water In Girls Toilet"),
        ('toiletwater_b', "Water In Boys Toilet"),
        ('toiletb_func', "Functional Boys Toilet"),
        ('toiletg_func', "Functional Girls Toilet"),
        ('urinals_b', "Boys Urinals"),
        ('urinals_g', "Girls Urinals"),
        ('handwash_count', "Handwash"),],

    'teacher':[('teacher',"No. Of Teachers")],

    'school':[('school',"No. Of School")],

    'student':[('student',"No. Of Student")],

    'security':[
        ('bndrywall_1', "Pucca"),
        ('bndrywall_2', "Pucca But Broken"),
        ('bndrywall_3', "Barbed wire fencing"),
        ('bndrywall_4', "Hedges"),
        ('bndrywall_5', "No Boundary wall"),
        ('bndrywall_6', "Others"),
        ('bndrywall_7', "Partial"),
        ('bndrywall_8', "Under Construction"),
    ],

    'school_management':[
        ('schmgt_1', 'Edu. Dept.'),
        ('schmgt_2', 'Tribal/social Welfare Dept.'),
        ('schmgt_3', 'Local Body'),
        ('schmgt_4', 'Pvt. Aided'),
        ('schmgt_5', 'Pvt. Unaided'),
        ('schmgt_6', 'Others'),
        ('schmgt_7', 'Central Gov'),
        ('schmgt_8', 'Unrecogised'),
        ('schmgt_97', 'Recog. Madarsa'),
        ('schmgt_98', 'Unrecog. Madarsa'),
    ],

    'school_category':[
        ('schcat_1', 'Pri. Only'),
        ('schcat_2', 'Pri. and Upper Pri.'),
        ('schcat_3', "Pri., Upper Pri., Sec. and Higher Sec."),
        ('schcat_4', 'Upper Pri.'),
        ('schcat_5', 'Upper Pri., Sec. and Higher Sec.'),
        ('schcat_6', "Pri., Upper Pri., Sec."),
        ('schcat_7', "Upper Pri.,Sec."),
        ('schcat_8', 'Sec.'),
        ('schcat_10', 'Sec. and Higher Sec.'),
        ('schcat_11', 'Higher Sec.'),
    ],
}

def plot_choropleth_maps(request):
    ft = json.dumps(features)
    names = districtSummary.objects.only('distname', 'distcode')
    names = serialize('json',names, fields=('distname', 'distcode'))

    dis_json = json.loads(names)
    _names = []
    for dist in dis_json:
        _names += [dist['fields']]

    js_dist = json.dumps(_names)
    return render(request,'ElementarySchool/chloropleth/choropleth-maps.html',context={'district':js_dist,"ft_data":json.dumps(features)})


klass = {
    'district':districtSummary,
    'taluka':blockSummary,
}

location = {
    'distname':'distname__iexact',
}

weights = {
    'water' : {'water_1':0.2,'water_2':0.2,'water_3':0.2,
                      'water_4':0.2,'water_5':0.2,},

           'sanitation':{
               'toiletwater_g':0.14,'toiletwater_b':0.14,'toiletb_func':0.14,
               'toiletg_func':0.14,'urinals_b':0.14,'urinals_g':0.14,
               'handwash_count':0.14,},

           'security':{
               'bndrywall_1':0.125,'bndrywall_2':0.125,'bndrywall_3':0.125,'bndrywall_4':0.125,
               'bndrywall_5':0.125,'bndrywall_6':0.125,'bndrywall_7':0.125,'bndrywall_8':0.125,
           },

           'school_management':{
               'schmgt_1':0.1,'schmgt_2':0.1,'schmgt_3':0.1,'schmgt_4':0.1,
               'schmgt_5':0.1,'schmgt_6':0.1,'schmgt_7':0.1,'schmgt_8':0.1,
               'schmgt_97':0.1,'schmgt_98':0.1,
           },

           'school_category':{
               'schcat_1':0.1,'schcat_2':0.1,'schcat_3':0.1,'schcat_4':0.1,
               'schcat_5':0.1,'schcat_6':0.1,'schcat_7':0.1,'schcat_8':0.1,
               'schcat_10':0.1,'schcat_11':0.1,
           },

           'teacher':{'teacher':1},

           'school': {'school':1},

           'student':{'student':1},
           }

colors = {
    'water':('#90c1f5','#2777ce'),
    'sanitation':('#cc9f67','#b46e18'),
    'security':('#d183e5','#9025ab'),
    'school_management':('#f938c4','#ae0a81'),
    'school_category':('#87f5aa','#3ba05b'),
    'teacher':('#e4f067','#949f23'),
    'school':('#9df5f0','#44aba5'),
    'student':('#f9906b','#b65330'),
}

@csrf_exempt
def get_map(request):
    if request.method == 'POST':
        if request.is_ajax():
            ip = json.loads(request.POST['data'])
            ##print ip
            ##Get Class Name##
            cls = klass[ip['kclass']]

            ##Feature_list
            ftr = features[ip['feature'][0]]

            ##color_range
            frm,to = Color(colors[ip['feature'][0]][0]),Color(colors[ip['feature'][0]][1])

            ##five ranges
            color_range = frm.range_to(to,6)

            wt = None
            ##get the weights
            if not ip['weight']:
                wt = weights[ip['feature'][0]]
            else:
                wt = ip['weight'].values()
                wt = {i[0]:float(i[1]) for i in wt}


            ##Filter Based On Location
            loc = ip['location']

            val_fields = ['geom']
            #val_fields.extend(loc.keys())

            if ip['kclass'] =='district':
                val_fields +=['distname']
            elif ip['kclass'] == 'taluka':
                val_fields += ['distname']
                val_fields += ['block_name']


            ##Get Field Names
            fl_val,fl_name = zip(*ftr)

            val_fields += list(fl_val)

            ##Creating QueryDict
            query_dict = {location[k]:v for k,v in loc.iteritems()}

            ##filter based on location
            query = cls.objects.all()

            for k,v in query_dict.iteritems():
               query = query.filter(**{k:v})


            query = query.values(*val_fields)
            result = query

            result= GeoJSONSerializer().serialize(result)

            dict_json = json.loads(result)
            #print dict_json
            #remove crs field
            dict_json.pop('crs', None)

            ind_lst = []
            dist_no_geom = []
            ## iterate over the features
            for feature_dict in dict_json['features']:

                ## pop out the properties and store it in props
                props = feature_dict.pop('properties',None)

                #print feature_dict

                ## remove location info and store in variables
                distname = ''
                talukaname = ''
                if props.has_key('distname'):
                    distname = props.pop('distname',None)

                if props.has_key('block_name'):
                    talukaname = props.pop('block_name',None)

                ##remaining pairs are the fields
                index = 0

                for k in props:
                    index += round(props[k]*wt[k],2)
                ind_lst += [index]

                temp = dict()
                if not feature_dict['geometry']:
                    if distname:
                        temp = {"district":distname,"index":round(index,2)}

                    if talukaname:
                        temp = {"district":distname,"taluka":talukaname,"index":round(index,2)}

                    #print temp
                    dist_no_geom += [temp]

                ## add the index
                feature_dict['properties'] = {}
                feature_dict['properties']['index'] = round(index,2)
                ## add the locations
                if distname:
                    feature_dict['properties']['distname'] = distname
                if talukaname:
                    feature_dict['properties']['taluka'] = talukaname

            min_v = max(0,floor(min(ind_lst))-1)
            max_v = floor(max(ind_lst))+1
            rg = round(max_v-min_v,2)
            grade = [round(min_v+(rg*(float(i)/100))) for i in range(0,120,20)]
            #print min_v,max_v
            #print grade
            color_range = [str(i) for i in color_range]
            #print color_range
            data = {
                'geographic_data':dict_json,
                'color':color_range,
                'grade':grade,
                'no_geom':dist_no_geom,
            }

            result = json.dumps(data)



        return HttpResponse(result)
    else:
        raise Http404("Access Denied!")
