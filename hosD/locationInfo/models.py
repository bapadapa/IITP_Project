from django.db import models
# Create your models here.

class LInfo(models.Model):
    loc_hosCode=models.IntegerField(primary_key= True) # PK
    loc_hosName = models.CharField(max_length=50) # �������
    loc_hosClassName = models.CharField(max_length=50) # �����ڵ��
    loc_hosCityName = models.CharField(max_length=50) # �õ��ڵ��
    loc_hosCountyName = models.CharField(max_length=50) # �ñ����ڵ��
    loc_zipCode = models.CharField(max_length=50) # �����ȣ
    loc_hosAddress = models.CharField(max_length=120) # �ּ�
    loc_hosPhoneNumber = models.CharField(max_length=50) # ��ȭ��ȣ
    loc_hosUrl = models.CharField(max_length=200) # ����URL
    loc_hosEstablishment = models.CharField(max_length=50) # ��������
    loc_Latitude = models.FloatField(null=True) # ����
    loc_longitude = models.FloatField(null=True) # �浵         
    def __str__(self):
        return self.loc_hosName  
    class Meta:
        verbose_name = 'locInfo'
        verbose_name_plural = 'locInfo'

