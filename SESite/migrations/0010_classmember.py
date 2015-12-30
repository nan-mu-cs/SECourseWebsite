# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0009_auto_20151227_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classmember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_info', models.ForeignKey(to='SESite.Class')),
                ('member', models.ForeignKey(to='SESite.Person')),
            ],
        ),
    ]
