# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MahaSchoolCentroidRti1314',
            fields=[
                ('fid', models.AutoField(serialize=False, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('district_n', models.CharField(max_length=50, null=True, blank=True)),
                ('taluka_nam', models.CharField(max_length=30, null=True, blank=True)),
                ('census_201', models.CharField(max_length=6, null=True, blank=True)),
                ('area_name', models.CharField(max_length=150, null=True, blank=True)),
                ('disname', models.CharField(max_length=60, null=True, blank=True)),
                ('blockname', models.CharField(max_length=60, null=True, blank=True)),
                ('villagenam', models.CharField(max_length=60, null=True, blank=True)),
                ('udisecode', models.CharField(max_length=11, null=True, blank=True)),
                ('schoolname', models.CharField(max_length=254, null=True, blank=True)),
                ('schcategor', models.CharField(max_length=60, null=True, blank=True)),
                ('pincode', models.CharField(max_length=6, null=True, blank=True)),
                ('lowclass', models.FloatField(null=True, blank=True)),
                ('highclass', models.FloatField(null=True, blank=True)),
                ('preprimary', models.FloatField(null=True, blank=True)),
                ('preprima_1', models.FloatField(null=True, blank=True)),
                ('medium', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'maha_school_centroid_rti_13_14',
                'managed': False,
            },
        ),
    ]
