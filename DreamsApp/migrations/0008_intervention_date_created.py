# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 05:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0007_auto_20161013_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
