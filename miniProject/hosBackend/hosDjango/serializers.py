from rest_framework.serializers import ModelSerializer
from hosDjango.models import LocInfo


class LocInfoSerializer(ModelSerializer):
    class Meta:
        # models의 LocInfo에 정의된 데이터를 이용한다
        model = LocInfo
        # 모든 필드를 이용한다.
        fields = '__all__'