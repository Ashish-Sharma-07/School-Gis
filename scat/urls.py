from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.scat, name='scat'),
    url(r'^new_form$', views.new_form, name='new_form'),
    url(r'^bookinlib$', views.bil, name='bkil'),

]