# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160325_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
    ]