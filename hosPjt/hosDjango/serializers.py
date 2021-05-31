from rest_framework.serializers import ModelSerializer
from .models import LocInfo

class LocSerializer(ModelSerializer):
    class Meta:
        model = LocInfo
        fields = '__all__'