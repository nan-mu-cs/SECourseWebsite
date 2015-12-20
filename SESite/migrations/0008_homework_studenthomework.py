# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import SESite.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SESite', '0007_courseintro_taintro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('due_time', models.DateTimeField()),
                ('assigner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Homework',
            },
        ),
        migrations.CreateModel(
            name='StudentHomework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('homeworkfile', models.FileField(upload_to=SESite.models.homework_upload_directory_path)),
                ('score', models.DecimalField(max_digits=4, decimal_places=1)),
                ('homeworkid', models.ForeignKey(to='SESite.Homework')),
                ('student_ID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'StudentHomework',
            },
        ),
    ]
