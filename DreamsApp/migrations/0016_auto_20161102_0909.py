# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-02 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0015_auto_20161102_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='landmark',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Land Mark near Residence'),
        ),
    ]
