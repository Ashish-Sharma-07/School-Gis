# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import SchoolInfo
from django.shortcuts import redirect
def details(request,d_id):
    if request.method == 'POST':
        id = request.POST.get['post_id',False]
        print "id"
    context = dict(all = SchoolInfo.objects.get(schcd=d_id))
    return render(request, 'details/details.html',context)

#"27080709301"