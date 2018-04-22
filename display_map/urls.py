from django.conf.urls import patterns, url
from django.conf import settings
from .views import index
app_name="displaym"
urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^index/$', index,name="display_map"),
    #url(r'^data.geojson$',GeoJSONLayerView.as_view(model=SchoolCentroid1314),name="data"),
  
)


