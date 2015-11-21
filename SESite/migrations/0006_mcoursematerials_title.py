# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0005_mcoursematerials'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcoursematerials',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 11, 21, 8, 54, 26, 235013, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
    ]
