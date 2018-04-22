from django import forms
from django.forms import formset_factory

from details.models import SchoolInfo

class cform(forms.Form):
    clst = tuple((a,a) for a in SchoolInfo._meta.get_all_field_names())
    olst = (
        ('exact', 'equal'),
        ('contains','contains'),
        ('gt','greater'),
        ('lt','less'),
        ('ne','noteq'),
    )
    clm = forms.ChoiceField(choices=clst,label='')
    optr = forms.ChoiceField(choices=olst,label='')
    inp = forms.CharField(max_length=100,label='',required=True)



