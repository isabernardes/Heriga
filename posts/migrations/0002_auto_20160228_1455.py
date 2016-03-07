# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timescape',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='updated',
        ),
    ]
