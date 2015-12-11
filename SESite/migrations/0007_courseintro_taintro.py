# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SESite', '0006_mcoursematerials_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseIntro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pre_intro', models.CharField(max_length=2000)),
                ('materi_intro', models.CharField(max_length=2000)),
                ('score_consti', models.CharField(max_length=2000)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CourseIntro',
            },
        ),
        migrations.CreateModel(
            name='TAIntro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_intro', models.CharField(max_length=2000)),
                ('ta_intro', models.CharField(max_length=2000)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TAIntro',
            },
        ),
    ]
