from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from core.models import Building, Crimes
from core.filters import BuildingCoordinatesFilter
from core.serializers import BuildingSerializer, CrimesSerializer


# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer


# class CrimesViewSet(viewsets.ModelViewSet):
#     queryset = Crimes.objects.all()
#     serializer_class = CrimesSerializer


class BuildingList(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('longitude', 'latitude', 'number', 'street', 'crimes__total')
    filter_class = BuildingCoordinatesFilter


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class CrimesList(generics.ListAPIView):
    queryset = Crimes.objects.all()
    serializer_class = CrimesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('building_id', 'year_month', 'total', 'total_points', 'bodily_harm_with_fatal_cons',
                     'brigandage', 'drugs', 'extortion', 'fraud', 'grave_and_very_grave', 'hooliganism',
                     'intentional_injury', 'looting', 'murder', 'rape', 'theft')


class CrimesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crimes.objects.all()
    serializer_class = CrimesSerializer
