# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_cnr'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnr',
            name='has_commented',
            field=models.BooleanField(default=False),
        ),
    ]
