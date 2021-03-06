# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-02 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DreamsApp', '0013_auto_20161027_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='age_at_enrollment',
            field=models.IntegerField(blank=True, default=10, null=True, verbose_name='Age at Enrollment'),
        ),
        migrations.AlterField(
            model_name='client',
            name='dss_id_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='DSS ID Number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name="Primary Care Giver/Guardian' Name"),
        ),
        migrations.AlterField(
            model_name='client',
            name='guardian_national_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='National ID (Care giver/Guardian)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='guardian_phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone Number(Care giver/Guardian)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='implementing_partner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DreamsApp.ImplementingPartner', verbose_name='Implementing Partner'),
        ),
        migrations.AlterField(
            model_name='client',
            name='informal_settlement',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Informal Settlement'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='relationship_with_guardian',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Relationship with Guardian'),
        ),
        migrations.AlterField(
            model_name='client',
            name='verification_doc_no',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Verification Doc No'),
        ),
        migrations.AlterField(
            model_name='client',
            name='verification_document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DreamsApp.VerificationDocument', verbose_name='Verification Document'),
        ),
    ]
