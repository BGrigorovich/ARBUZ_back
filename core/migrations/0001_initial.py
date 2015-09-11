# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('latitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Crimes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year_month', models.CharField(max_length=8)),
                ('total', models.IntegerField()),
                ('total_points', models.IntegerField()),
                ('bodily_harm_with_fatal_cons', models.IntegerField()),
                ('brigandage', models.IntegerField()),
                ('drugs', models.IntegerField()),
                ('extortion', models.IntegerField()),
                ('fraud', models.IntegerField()),
                ('grave_and_very_grave', models.IntegerField()),
                ('hooliganism', models.IntegerField()),
                ('intentional_injury', models.IntegerField()),
                ('looting', models.IntegerField()),
                ('murder', models.IntegerField()),
                ('rape', models.IntegerField()),
                ('theft', models.IntegerField()),
                ('building', models.ForeignKey(to='core.Building')),
            ],
        ),
    ]
