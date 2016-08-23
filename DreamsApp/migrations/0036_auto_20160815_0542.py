# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-15 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0035_auto_20160813_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='county', to='DreamsApp.County', verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='grievance_nature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievance_nature', to='DreamsApp.GrievanceNature', verbose_name='Nature of Grievance'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='implementing_partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DreamsApp.ImplementingPartner', verbose_name='Implementing Partner'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='received_by',
            field=models.CharField(max_length=250, verbose_name='Name of DREAMS staff receiving the grievance'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='reporter_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter_category', to='DreamsApp.GrievanceReporterCategory', verbose_name='Reporter Category'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='reporter_name',
            field=models.CharField(max_length=250, verbose_name='Reporter Name'),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ward', to='DreamsApp.Ward', verbose_name='Ward'),
        ),
    ]
