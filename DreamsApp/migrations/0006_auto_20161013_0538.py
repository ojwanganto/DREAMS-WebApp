# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0005_auto_20161013_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='date_changed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
