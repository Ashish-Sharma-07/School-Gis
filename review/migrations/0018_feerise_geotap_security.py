# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0017_cnr_school_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeRise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schcd', models.CharField(max_length=200, null=True, blank=True)),
                ('grade_1_admission_fee_rs_per_month', models.BigIntegerField(null=True, blank=True)),
                ('elementary_admission_fee', models.BigIntegerField(null=True, blank=True)),
                ('secondary_admission_fee', models.BigIntegerField(null=True, blank=True)),
                ('higher_secondary_admission_fee', models.BigIntegerField(null=True, blank=True)),
                ('raise_in_fee_within_last_year', models.BigIntegerField(null=True, blank=True)),
                ('from_2_yrs_to_last_year', models.BigIntegerField(null=True, blank=True)),
                ('from_3_yrs_to_2_yrs_ago', models.BigIntegerField(null=True, blank=True)),
                ('is_PTA_formed', models.BigIntegerField(null=True, blank=True)),
                ('is_PTA_elected_or_selected', models.CharField(max_length=20)),
                ('is_representative_or_management', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GeoTap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schcd', models.CharField(max_length=200, null=True, blank=True)),
                ('photo_frontside', models.FileField(upload_to='documents/frontside/%Y-%m-%d/')),
                ('photo_classroom', models.FileField(upload_to='documents/clsroom/%Y-%m-%d/')),
                ('photo_toilet_1', models.FileField(upload_to='documents/toilet_1/%Y-%m-%d/')),
                ('photo_toilet_2', models.FileField(null=True, upload_to='documents/toilet_2/%Y-%m-%d/')),
                ('photo_toilet_3', models.FileField(null=True, upload_to='documents/toilet_3/%Y-%m-%d/')),
                ('photo_playground', models.FileField(upload_to='documents/playgrnd/%Y-%m-%d/')),
                ('photo_showing_DISE_code', models.FileField(upload_to='documents/DISE/%Y-%m-%d/')),
                ('photo_on_common_prayer', models.FileField(upload_to='documents/common_pryr/%Y-%m-%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schcd', models.CharField(max_length=200, null=True, blank=True)),
                ('is_security_adequate', models.BigIntegerField(null=True, blank=True)),
                ('any_police_case_in_last_6_months', models.BigIntegerField(null=True, blank=True)),
                ('if_yes_FIR_no', models.CharField(max_length=150, null=True, blank=True)),
                ('if_yes_police_station_ID', models.CharField(max_length=150, null=True, blank=True)),
                ('is_CCTV_installed', models.BigIntegerField(null=True, blank=True)),
                ('is_CCTV_monitored', models.BigIntegerField(null=True, blank=True)),
                ('if_yes_name_and_designation', models.CharField(max_length=150, null=True, blank=True)),
                ('are_boundary_walls_in_toilet', models.BigIntegerField(null=True, blank=True)),
                ('comment', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
