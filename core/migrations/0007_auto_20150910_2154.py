# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150910_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='id',
            new_name='building_id',
        ),
        migrations.RenameField(
            model_name='crimes',
            old_name='id',
            new_name='crimes_id',
        ),
    ]
