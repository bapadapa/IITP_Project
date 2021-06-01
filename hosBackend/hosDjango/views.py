from django.db.models import query
from django.http import response
from django.shortcuts import render
from hosDjango import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hosDjango.models import LocInfo
from hosDjango.serializers import LocInfoSerializer

# Create your views here.
class LocInfoViewSet(ModelViewSet):
    queryset = LocInfo.objects.all()
    serializer_class = LocInfoSerializer


@api_view(['get'])
def cityHos(request,city):
    queryset =LocInfo.objects.filter(loc_hosCityName = city)
    serializer = LocInfoSerializer(queryset , many = True)
    return Response(serializer.data)

@api_view(['get'])
def CounryHos(request,county):
    queryset =LocInfo.objects.filter(loc_hosCountyName = county)
    serializer = LocInfoSerializer(queryset , many = True)
    return Response(serializer.data)

@api_view(['get'])
def cityCountryHos(request,city,county):
    queryset =LocInfo.objects.filter(loc_hosCityName = city,loc_hosCountyName = county)
    serializer = LocInfoSerializer(queryset , many = True)
    return Response(serializer.data)
    
@api_view(['get'])
def AllHos(request,city ,county , subject):
    queryset =LocInfo.objects.filter(
        loc_hosCityName = city,loc_hosCountyName = county,loc_hosClassName = subject
        )
    serializer = LocInfoSerializer(queryset , many = True)
    return Response(serializer.data)



# def selectCity(request, city):
#     qs = LocInfo.objects.get(loc_hosCityName = city)
#     context = {'info': qs}
#     return context



