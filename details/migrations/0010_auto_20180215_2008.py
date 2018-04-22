# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0009_auto_20180215_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfo',
            name='ppstudent',
            field=models.IntegerField(null=True),
        ),
    ]
