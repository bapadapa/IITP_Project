from django.db import models
# Create your models here.

class LInfo(models.Model):
    loc_hosCode=models.IntegerField(primary_key= True) # PK
    loc_hosName = models.CharField(max_length=50) # 요양기관명
    loc_hosClassName = models.CharField(max_length=50) # 종별코드명
    loc_hosCityName = models.CharField(max_length=50) # 시도코드명
    loc_hosCountyName = models.CharField(max_length=50) # 시군구코드명
    loc_zipCode = models.CharField(max_length=50) # 우편번호
    loc_hosAddress = models.CharField(max_length=120) # 주소
    loc_hosPhoneNumber = models.CharField(max_length=50) # 전화번호
    loc_hosUrl = models.CharField(max_length=200) # 병원URL
    loc_hosEstablishment = models.CharField(max_length=50) # 개설일자
    loc_Latitude = models.FloatField(null=True) # 위도
    loc_longitude = models.FloatField(null=True) # 경도         
    def __str__(self):
        return self.loc_hosName  
    class Meta:
        verbose_name = 'locInfo'
        verbose_name_plural = 'locInfo'

