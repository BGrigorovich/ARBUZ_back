import django_filters
from .models import Building


class BuildingFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(name="building_id", lookup_type="contains")

    class Meta:
            model = Building
            fields = ['building_id']
