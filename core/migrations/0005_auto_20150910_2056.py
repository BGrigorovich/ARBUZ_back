# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150910_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='building',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
