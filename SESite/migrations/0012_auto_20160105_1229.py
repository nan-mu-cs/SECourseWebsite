# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0011_auto_20160104_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseintro',
            name='classid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='mcoursematerials',
            name='classid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='noticemessage',
            name='classid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='taintro',
            name='classid',
            field=models.IntegerField(default=1),
        ),
    ]
