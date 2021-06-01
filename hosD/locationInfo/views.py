from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import LInfo
from .serializers import LInfoSerializer
# Create your views here.

class LInfoViewSets(ModelViewSet):
    queryset = LInfo.objects.all()
    serializer_class = LInfoSerializer
