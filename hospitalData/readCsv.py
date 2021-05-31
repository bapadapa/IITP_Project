import pandas as pd
import os


hospital_LocInfo = pd.read_csv('./hospitalData/hospital_LocInfo.csv', encoding='utf-8')



# 한국 시코드명
cityName = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', 
    '부산', '서울', '세종시', '울산', '인천', '전남', '전북', '제주', '충남', '충북']

# 지역별 코드부여 100000단위로 추가
cityCode =[]
for i in range(len(cityName)):
    cityCode.append((i+1)*100000)   

# 딕셔너리로 변경
cityName_dic = {string : i for i,string in enumerate(cityName)}

# 비교하여 코드 부여
CityCodeList = []
for i,rows in hospital_LocInfo.iterrows():    
    cityIndex = cityName.index(rows['시도코드명'])
    CityCodeList.append( cityCode[cityIndex])
    cityCode[cityIndex]+=1

hospital_LocInfo['hosCode'] = CityCodeList
# Index(['암호화YKIHO코드', '요양기관명', '종별코드', '종별코드명', '시도코드', '시도코드명', '시군구코드',
#        '시군구코드명', '읍면동', '우편번호', '주소', '전화번호', '병원URL', '개설일자', 'x좌표', 'y좌표',
#        '총의사수', '일반의 인원수', '인턴 인원수', '레지던트 인원수', '전문의 인원수'],
#       dtype='object')

# 필요 칼럼만 추출
postHospitalLocInfo = hospital_LocInfo[['hosCode','요양기관명', '종별코드', '종별코드명', '시도코드', 
'시도코드명', '시군구코드', '시군구코드명', '우편번호', '주소', '전화번호', '병원URL', '개설일자', 'x좌표', 'y좌표']]

# 칼럼 영문으로 변경!
postHospitalLocInfo.columns = ['hosCode','hosName','hosClassCode','hosClassName','hosCityCode','hosCityName'
'hosCountyCode','hosCountyName','zipCode','hosAddress','hosPhoneNumber','hosUrl','hosEstablishment',
'Latitude','longitude']

print(postHospitalLocInfo)

# ---------------------------------------
# 병원 상세정보
# hospital_Info = pd.read_csv('./hospitalData/hospital_Info.csv', encoding='utf-8')


# ['암호화YKIHO코드','요양기관명',	'진료과목코드',	'진료과목코드명'	,'과목별' ,'전문의수',	'선택진료', '의사수']

