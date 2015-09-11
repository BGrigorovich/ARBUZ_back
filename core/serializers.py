from rest_framework import serializers
from .models import Building, Crimes


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('building_id', 'longitude', 'latitude', 'number', 'street')


class CrimesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crimes
        fields = ('crimes_id', 'year_month', 'total', 'total_points', 'bodily_harm_with_fatal_cons',
                  'brigandage', 'drugs', 'extortion', 'fraud', 'grave_and_very_grave', 'hooliganism',
                  'intentional_injury', 'looting', 'murder', 'rape', 'theft')
