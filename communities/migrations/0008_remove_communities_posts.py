# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-05-21 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0007_communities_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='communities',
            name='posts',
        ),
    ]
