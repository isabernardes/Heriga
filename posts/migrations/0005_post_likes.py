# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160420_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]