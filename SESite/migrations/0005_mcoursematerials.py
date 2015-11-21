# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import SESite.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SESite', '0004_noticemessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='mCourseMaterials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('docfile', models.FileField(upload_to=SESite.models.coursematerials_upload_directory_path)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CourseMaterials',
            },
        ),
    ]
