import django_filters
from .models import Building, Crimes


class BuildingCoordinatesFilter(django_filters.FilterSet):
    latitude_less = django_filters.NumberFilter(name="latitude", lookup_type="lte")
    latitude_greater = django_filters.NumberFilter(name="latitude", lookup_type="gte")
    longitude_less = django_filters.NumberFilter(name="longitude", lookup_type="lte")
    longitude_greater = django_filters.NumberFilter(name="longitude", lookup_type="gte")

    class Meta:
        model = Building
        fields = ['latitude_less', 'latitude_greater', 'longitude_less', 'longitude_greater']


class CrimesFilter(django_filters.FilterSet):
    month = django_filters.DateFilter(name="month_year")

    class Meta:
        model = Crimes
        fields = ['month']
