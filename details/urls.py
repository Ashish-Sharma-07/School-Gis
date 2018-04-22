from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'details'

urlpatterns = [
    #/detail_id/
    url(r'^(?P<d_id>[0-9]+)/$', views.details, name='details'),
]