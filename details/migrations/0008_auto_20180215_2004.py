# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_auto_20180207_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolinfo',
            options={'managed': True},
        ),
    ]
