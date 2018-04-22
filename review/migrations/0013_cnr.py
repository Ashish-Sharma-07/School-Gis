# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_delete_cnr'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_id', models.IntegerField()),
                ('u_name', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('u_rating', models.IntegerField()),
            ],
        ),
    ]
