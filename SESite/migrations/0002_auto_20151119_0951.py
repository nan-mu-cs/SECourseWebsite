# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SESite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=2000)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'NoticeMessage',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AlterField(
            model_name='person',
            name='idnum',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
