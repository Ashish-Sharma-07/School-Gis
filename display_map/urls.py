

from django.conf.urls import patterns, url
from django.conf import settings
from .views import index
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from display_map.models import MahaSchoolCentroidRti1314

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^index/$', index),
    #url(r'^data.geojson$',GeoJSONLayerView.as_view(model=SchoolCentroid1314),name="data"),
  
)


