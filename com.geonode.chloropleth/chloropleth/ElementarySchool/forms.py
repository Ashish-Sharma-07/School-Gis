from django import forms
from .models import state_maharashtra

class AttributeForm(forms.Form):
    level = (
        ('district','District'),
        ('taluka','Taluka'),
    )

    district = tuple([(i['district'],i['district']) for i in state_maharashtra.objects.values('district').all()])
    feature = (
        ('ppteacher','Teacher'),
        ('water','Water'),
        ('ppstudent','Student'),
    )

    get_level = forms.ChoiceField(label='Level',choices=level,initial='district')
    get_district = forms.ChoiceField(label='District',choices=district,disabled=True)
    get_feature = forms.ChoiceField(label='Feature',choices = feature)