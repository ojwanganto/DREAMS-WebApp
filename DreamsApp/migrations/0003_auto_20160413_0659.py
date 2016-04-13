# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0002_auto_20160412_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='interventiontype',
            name='has_ccc_number',
            field=models.BooleanField(default=False, verbose_name='Intervention collects CCC details'),
        ),
        migrations.AddField(
            model_name='interventiontype',
            name='has_no_of_sessions',
            field=models.BooleanField(default=False, verbose_name='Intervention collects No. of sessions'),
        ),
        migrations.AlterField(
            model_name='interventiontype',
            name='has_hts_result',
            field=models.BooleanField(default=False, verbose_name='Intervention collects HTS Result'),
        ),
        migrations.AlterField(
            model_name='interventiontype',
            name='has_pregnancy_result',
            field=models.BooleanField(default=False, verbose_name='Intervention collects Pregnancy Result'),
        ),
    ]
