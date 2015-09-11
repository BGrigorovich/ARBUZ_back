# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150910_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
