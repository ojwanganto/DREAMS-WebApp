# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0009_intervention_date_changed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='date_changed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
