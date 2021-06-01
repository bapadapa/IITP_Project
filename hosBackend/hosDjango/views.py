from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from hosDjango.models import LocInfo
from hosDjango.serializers import LocInfoSerializer

# Create your views here.
class LocInfoViewSet(ModelViewSet):
    queryset = LocInfo.objects.all()
    serializer_class = LocInfoSerializer