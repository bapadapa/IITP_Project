from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import LocInfo
from .serializers import LocSerializer

# Create your views here.
class LocViewSet(ModelViewSet):
    queryset = LocInfo.objects.all()
    serializer_class =LocSerializer