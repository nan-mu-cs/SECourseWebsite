# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0002_auto_20151119_0951'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NoticeMessage',
        ),
    ]
