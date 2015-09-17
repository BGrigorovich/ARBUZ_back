from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


class Building(models.Model):
    building_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()


class Crimes(models.Model):
    crimes_id = models.IntegerField(primary_key=True)
    building_id = models.ForeignKey(Building, related_name='crimes')
    year_month = models.DateField(max_length=8)
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


from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):

    # for user in User.objects.all():
    #     Token.objects.get_or_create(user=user)
    if created:
        Token.objects.create(user=instance)
