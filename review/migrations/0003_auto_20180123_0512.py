# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='auth_user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
