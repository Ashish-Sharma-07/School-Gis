# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20180207_1237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolinfo',
            options={'managed': False},
        ),
    ]
