# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20170424_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
