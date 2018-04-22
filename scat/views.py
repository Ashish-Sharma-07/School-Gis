from django.shortcuts import render, render_to_response
from details.views import SchoolInfo
from django.db.models import Q
from .forms import cform

comp_filter = []
comp_inp= []
i=0

def scat(request):
    global comp_filter,comp_inp,i
    print comp_filter
    query={}
    cname = SchoolInfo._meta.get_all_field_names()
    form = cform()
    context = dict(cname=cname, form=form)
    if request.method == 'POST':
        form = cform(data=request.POST)
        if form.is_valid():
            clm = form.cleaned_data['clm']
            optr = form.cleaned_data['optr']
            inp = form.cleaned_data['inp']
            if not comp_filter:
                comp_filter.append(clm + '__' + optr)
                print comp_filter[i]
                comp_inp.append(inp)
                c={ '{0}'.format(comp_filter[i]):inp }
                stds = SchoolInfo.objects.filter(**c)
                context = dict(stds=stds)
                i+=1
                return render(request,'scat/data.html',context)
            else:
                comp_filter.append(clm + '__' + optr)
                comp_inp.append(inp)
                print comp_filter
                for index,cf in enumerate(comp_filter):
                    query.update({'{0}'.format(cf):comp_inp[index]  })
                print query
                stds = SchoolInfo.objects.filter(**query)
                context = dict(stds=stds)
                return render(request, 'scat/data.html', context)
    else:
        comp_filter = []
        comp_inp = []
        i = 0
    return render(request, 'scat/scat.html',context)

def new_form(request):
    form=cform()
    context = dict(form=form)
    print "fluxi"
    return render_to_response('scat/form.html',context)


def bil(request):
    context = dict(stds=SchoolInfo.objects.filter(~Q(bookinlib='0')).order_by('-bookinlib')[:20])
    return render(request, 'scat/scat.html',context)