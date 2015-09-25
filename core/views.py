from django_filters import FilterSet
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication

from core.models import Building, Crimes
from core.filters import BuildingCoordinatesFilter, CrimesFilter
from core.serializers import BuildingSerializer, CrimesSerializer


# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer


# class CrimesViewSet(viewsets.ModelViewSet):
#     queryset = Crimes.objects.all()
#     serializer_class = CrimesSerializer


class BuildingList(generics.ListAPIView):
    pagination_class = PageNumberPagination
    authentication_classes = (BasicAuthentication,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_class = BuildingCoordinatesFilter


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class CrimesList(generics.ListAPIView):
    queryset = Crimes.objects.all()
    serializer_class = CrimesSerializer
    # filter_class = CrimesFilter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('building_id', 'year_month', 'total', 'total_points', 'bodily_harm_with_fatal_cons',
                     'brigandage', 'drugs', 'extortion', 'fraud', 'grave_and_very_grave', 'hooliganism',
                     'intentional_injury', 'looting', 'murder', 'rape', 'theft')


class CrimesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crimes.objects.all()
    serializer_class = CrimesSerializer
