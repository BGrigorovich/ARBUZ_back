import datetime
# from datetime import datetime
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication

from core.models import Building, Crimes
from core.filters import BuildingCoordinatesFilter
from core.serializers import BuildingSerializer, CrimesSerializer
from django.db.models import Q


# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer


# class CrimesViewSet(viewsets.ModelViewSet):
#     queryset = Crimes.objects.all()
#     serializer_class = CrimesSerializer


class BuildingList(generics.ListAPIView):
    pagination_class = PageNumberPagination
    authentication_classes = (BasicAuthentication,)
    serializer_class = BuildingSerializer
    filter_class = BuildingCoordinatesFilter
    queryset = Building.objects.all()
    # queryset = Building.objects.get(building_id=1)

    def filter_queryset(self, queryset):
        if self.request.GET.get('crimes__year_month') is not None:
            month = datetime.datetime.strptime(self.request.GET.get('crimes__year_month'), '%Y-%m-%d')
            return queryset.crimes.filter(year_month=month)
        else:
            return queryset
        # return queryset.crimes.filter(year_month=self.kwargs['crimes__year_month'])
        # return queryset.crimes_set.filter(year_month=self.request.GET.params['month'])
        # return queryset.crimes.filter(crimes__year_month=self.kwargs['crimes__year_month'])


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
