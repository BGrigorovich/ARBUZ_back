from rest_framework import serializers
from .models import Building, Crimes


# class FilteredCrimesSerializer(serializers.ListSerializer):
#     def to_representation(self, data):
#         data = data.filter(year_month=self.request.GET.get('crimes__year_month'), '%Y-%m-%d')
#         return super(FilteredCrimesSerializer, self).to_representation(data)


class CrimesSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = Crimes.objects.filter(year_month=self.request.GET.get('crimes__year_month'), '%Y-%m-%d')
        return data

    class Meta:
        # list_serializer_class = FilteredCrimesSerializer
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
