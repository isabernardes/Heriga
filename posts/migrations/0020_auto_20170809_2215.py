# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-09 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20170807_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
