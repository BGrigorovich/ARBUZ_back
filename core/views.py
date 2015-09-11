from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Building, Crimes
from core.filters import BuildingFilter
from core.serializers import BuildingSerializer, CrimesSerializer


# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer


# class CrimesViewSet(viewsets.ModelViewSet):
#     queryset = Crimes.objects.all()
#     serializer_class = CrimesSerializer


class BuildingList(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class BuildingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# class BuildingList(generics.ListAPIView):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer
#     filter_class = BuildingFilter
#
#     def get_queryset(self):
#         queryset = Building.objects.all()
#         id = self.request.query_params.get('building_id', None)
#         # longitude = self.request.query_params.get('longitude')
#         # latitude = self.request.query_params.get('latitude')
#         if id is not None:
#             queryset = queryset.filter(building_id=id)
#         return queryset


class CrimesList(APIView):
    def get(self, request, format=None):
        snippets = Crimes.objects.all()
        serializer = CrimesSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CrimesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrimesDetails(APIView):
    def get_object(self, pk):
        try:
            return Crimes.objects.get(pk=pk)
        except Crimes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        building = self.get_object(pk)
        serializer = CrimesSerializer(building)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CrimesSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
