# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_auto_20180215_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfo',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
