# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20170424_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
