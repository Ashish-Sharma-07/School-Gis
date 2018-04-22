from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from views import plot_choropleth_maps,get_map
app_name= 'district'

urlpatterns = [
	url(r'^$',plot_choropleth_maps,name="plt_maps"),
    	url(r'get-data/', get_map, name="get_data"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
