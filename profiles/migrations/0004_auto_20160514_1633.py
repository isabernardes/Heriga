# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-14 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160514_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergeneralinformation',
            name='cityOfBirth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralinformation',
            name='cityofResidence',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralinformation',
            name='countryOfBirth',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usergeneralinformation',
            name='countryofResidence',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userlanguages',
            name='languages',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userqualifications',
            name='university',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
