# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0014_mtinfo_classid'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='classid',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='studenthomework',
            name='classid',
            field=models.IntegerField(default=4),
        ),
    ]
