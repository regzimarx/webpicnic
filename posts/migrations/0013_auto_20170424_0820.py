# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 08:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_post_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 24, 8, 20, 45, 589506)),
            preserve_default=False,
        ),
    ]
