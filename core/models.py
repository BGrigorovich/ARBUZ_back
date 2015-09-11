from django.db import models


class Building(models.Model):
    building_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()


class Crimes(models.Model):
    crimes_id = models.IntegerField(primary_key=True)
    building_id = models.ForeignKey(Building)
    year_month = models.CharField(max_length=8)
    total = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    bodily_harm_with_fatal_cons = models.IntegerField(default=0)
    brigandage = models.IntegerField(default=0)
    drugs = models.IntegerField(default=0)
    extortion = models.IntegerField(default=0)
    fraud = models.IntegerField(default=0)
    grave_and_very_grave = models.IntegerField(default=0)
    hooliganism = models.IntegerField(default=0)
    intentional_injury = models.IntegerField(default=0)
    looting = models.IntegerField(default=0)
    murder = models.IntegerField(default=0)
    rape = models.IntegerField(default=0)
    theft = models.IntegerField(default=0)