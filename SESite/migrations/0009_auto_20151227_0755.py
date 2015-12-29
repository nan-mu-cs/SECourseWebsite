# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SESite', '0008_homework_studenthomework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_time', models.CharField(max_length=128)),
                ('classroom', models.CharField(max_length=128)),
                ('class_name', models.CharField(max_length=128)),
                ('teacher', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Class',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='joined_class',
            field=models.ManyToManyField(to='SESite.Class'),
        ),
    ]
