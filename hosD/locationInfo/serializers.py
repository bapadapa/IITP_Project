from .models import LInfo
from rest_framework.viewsets import ModelViewSet


class LInfoSerializer(ModelViewSet):
    class meta:
        model = LInfo
        fields = '__all__'