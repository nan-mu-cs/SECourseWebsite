# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0012_auto_20160105_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
    ]
