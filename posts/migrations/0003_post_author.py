# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170421_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
