# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0013_remove_class_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtinfo',
            name='classid',
            field=models.IntegerField(default=4),
        ),
    ]
