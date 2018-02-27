# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class MahaSchoolCentroidRti1314(models.Model):
    fid = models.AutoField(primary_key=True)
    geom = models.PointField(blank=True, null=True)
    district_n = models.CharField(max_length=50, blank=True, null=True)
    taluka_nam = models.CharField(max_length=30, blank=True, null=True)
    census_201 = models.CharField(max_length=6, blank=True, null=True)
    area_name = models.CharField(max_length=150, blank=True, null=True)
    disname = models.CharField(max_length=60, blank=True, null=True)
    blockname = models.CharField(max_length=60, blank=True, null=True)
    villagenam = models.CharField(max_length=60, blank=True, null=True)
    udisecode = models.CharField(max_length=11, blank=True, null=True)
    schoolname = models.CharField(max_length=254, blank=True, null=True)
    schcategor = models.CharField(max_length=60, blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    lowclass = models.FloatField(blank=True, null=True)
    highclass = models.FloatField(blank=True, null=True)
    preprimary = models.FloatField(blank=True, null=True)
    preprima_1 = models.FloatField(blank=True, null=True)
    medium = models.CharField(max_length=60, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'maha_school_centroid_rti_13_14'



