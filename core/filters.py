import django_filters as filters
from .models import Building, Crimes
# import rest_framework_filters as filters


class CrimesFilter(filters.FilterSet):
    month = filters.DateFilter(name='month')

    class Meta:
        model = Crimes
        fields = ['month']


class BuildingCoordinatesFilter(filters.FilterSet):
    latitude_less = filters.NumberFilter(name='latitude', lookup_type='lte')
    latitude_greater = filters.NumberFilter(name='latitude', lookup_type='gte')
    longitude_less = filters.NumberFilter(name='longitude', lookup_type='lte')
    longitude_greater = filters.NumberFilter(name='longitude', lookup_type='gte')
    # month = filters.RelatedFilter(CrimesFilter, name='month')

    class Meta:
        model = Building
        fields = ['latitude_less', 'latitude_greater', 'longitude_less', 'longitude_greater',
                  'longitude', 'latitude', 'number', 'street']
