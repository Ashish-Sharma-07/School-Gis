# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_auto_20180124_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNR',
            fields=[
                ('u_rating', models.IntegerField()),
                ('u_id', models.IntegerField(serialize=False, primary_key=True)),
                ('school_id', models.IntegerField()),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='school_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_id', models.IntegerField()),
                ('school_name', models.CharField(max_length=100)),
                ('school_info', models.TextField()),
            ],
        ),
    ]
