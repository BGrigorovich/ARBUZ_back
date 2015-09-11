from rest_framework import viewsets

from rest_framework import generics
from core.models import Building, Crimes
from core.filters import BuildingFilter
from core.serializers import BuildingSerializer, CrimesSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class CrimesViewSet(viewsets.ModelViewSet):
    queryset = Crimes.objects.all()
    serializer_class = CrimesSerializer


class BuildingList(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_class = BuildingFilter

    def get_queryset(self):
        queryset = Building.objects.all()
        id = self.request.query_params.get('building_id', None)
        # longitude = self.request.query_params.get('longitude')
        # latitude = self.request.query_params.get('latitude')
        if id is not None:
            queryset = queryset.filter(building_id=id)
        return queryset
