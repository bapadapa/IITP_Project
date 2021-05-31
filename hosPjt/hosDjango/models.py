
from django.db import models
# Create your models here.
class LocInfo(models.Model):
    loc_hosCode=models.IntegerField(primary_key= True) # PK
    loc_hosName = models.CharField(max_length=50) # 요양기관명
    loc_hosClassName = models.CharField(max_length=50) # 종별코드명
    loc_hosCityName = models.CharField(max_length=50) # 시도코드명
    loc_hosCountyName = models.CharField(max_length=50) # 시군구코드명
    loc_zipCode = models.CharField(max_length=50) # 우편번호
    loc_hosAddress = models.CharField(max_length=50) # 주소
    loc_hosPhoneNumber = models.CharField(max_length=50) # 전화번호
    loc_hosUrl = models.CharField(max_length=50) # 병원URL
    loc_hosEstablishment = models.CharField(max_length=50) # 개설일자
    loc_Latitude = models.FloatField() # 위도
    loc_longitude = models.FloatField() # 경도     
    def __str__(self):
        return self.loc_hosName
