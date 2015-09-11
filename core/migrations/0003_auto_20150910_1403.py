# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150910_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimes',
            name='bodily_harm_with_fatal_cons',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='brigandage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='drugs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='extortion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='fraud',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='grave_and_very_grave',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='hooliganism',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='intentional_injury',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='looting',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='murder',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='rape',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='theft',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='crimes',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]
