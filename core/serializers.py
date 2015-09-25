from rest_framework import serializers
from .models import Building, Crimes


class CrimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crimes
        fields = ('crimes_id',
                  'building_id',
                  'year_month',
                  'total',
                  'total_points',
                  'bodily_harm_with_fatal_cons',
                  'brigandage',
                  'drugs',
                  'extortion',
                  'fraud',
                  'grave_and_very_grave',
                  'hooliganism',
                  'intentional_injury',
                  'looting',
                  'murder',
                  'rape',
                  'theft')


class BuildingSerializer(serializers.ModelSerializer):
    crimes = CrimesSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('building_id',
                  'longitude',
                  'latitude',
                  'number',
                  'street',
                  'crimes')
