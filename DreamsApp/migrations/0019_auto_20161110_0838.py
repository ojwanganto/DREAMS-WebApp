# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-10 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0018_auto_20161109_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='verification_document_other',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Verification Document(Other)'),
        ),
        migrations.AlterField(
            model_name='clientsexualactivitydata',
            name='has_sexual_partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='DreamsApp.CategoricalResponse', verbose_name='Has current sexual partner'),
        ),
    ]
