# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
