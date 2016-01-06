# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import SESite.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0010_classmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='mtInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=10000)),
                ('tid', models.CharField(default=0, unique=True, max_length=128)),
                ('photo', models.ImageField(default=b'0', upload_to=SESite.models.picture_upload_directory_path)),
            ],
            options={
                'db_table': 'tInfo',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='joined_class',
        ),
        migrations.AlterField(
            model_name='classmember',
            name='member',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
