from rest_framework.serializers import ModelSerializer
from hosDjango.models import LocInfo

class LocInfoSerializer(ModelSerializer):
    class Meta:
        model = LocInfo
        fields = '__all__'