
from django.db import models
# Create your models here.
class LocInfo(models.Model):
    loc_hosCode=models.IntegerField(primary_key= True) # PK
    loc_hosName = models.CharField(max_length=50) # �������
    loc_hosClassName = models.CharField(max_length=50) # �����ڵ��
    loc_hosCityName = models.CharField(max_length=50) # �õ��ڵ��
    loc_hosCountyName = models.CharField(max_length=50) # �ñ����ڵ��
    loc_zipCode = models.CharField(max_length=50) # �����ȣ
    loc_hosAddress = models.CharField(max_length=50) # �ּ�
    loc_hosPhoneNumber = models.CharField(max_length=50) # ��ȭ��ȣ
    loc_hosUrl = models.CharField(max_length=50) # ����URL
    loc_hosEstablishment = models.CharField(max_length=50) # ��������
    loc_Latitude = models.FloatField() # ����
    loc_longitude = models.FloatField() # �浵     
    def __str__(self):
        return self.loc_hosName
