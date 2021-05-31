import pandas as pd
import numpy as np
import os

from pandas.core.frame import DataFrame


def extractLoc():
    hospital_LocInfo = pd.read_csv('./hospitalData/hospital_LocInfo.csv', encoding='utf-8')   
    # �븳援� �떆肄붾뱶紐�
    # cityName = ['媛뺤썝', '寃쎄린', '寃쎈궓', '寃쎈턿', '愿묒＜', '���援�', '����쟾', 
    #     '遺��궛', '�꽌�슱', '�꽭醫낆떆', '�슱�궛', '�씤泥�', '�쟾�궓', '�쟾遺�', '�젣二�', '異⑸궓', '異⑸턿']
    cityName = hospital_LocInfo['�떆�룄肄붾뱶紐�'].unique().tolist()
    
    # 吏��뿭蹂� 肄붾뱶遺��뿬 100000�떒�쐞濡� 異붽��
    cityCode =[]
    for i in range(len(cityName)):
        cityCode.append((i+1)*100000)   

    # �뵓�뀛�꼫由щ줈 蹂�寃�
    # cityName_dic = {string : i for i,string in enumerate(cityName)}

    # 鍮꾧탳�븯�뿬 肄붾뱶 遺��뿬
    CityCodeList = []
    for i,rows in hospital_LocInfo.iterrows():    
        cityIndex = cityName.index(rows['�떆�룄肄붾뱶紐�'])
        CityCodeList.append( cityCode[cityIndex])
        cityCode[cityIndex]+=1

    hospital_LocInfo['hosCode'] = CityCodeList
    # Index(['�븫�샇�솕YKIHO肄붾뱶', '�슂�뼇湲곌��紐�', '醫낅퀎肄붾뱶', '醫낅퀎肄붾뱶紐�', '�떆�룄肄붾뱶', '�떆�룄肄붾뱶紐�', '�떆援곌뎄肄붾뱶',
    #        '�떆援곌뎄肄붾뱶紐�', '�쓭硫대룞', '�슦�렪踰덊샇', '二쇱냼', '�쟾�솕踰덊샇', '蹂묒썝URL', '媛쒖꽕�씪�옄', 'x醫뚰몴', 'y醫뚰몴',
    #        '珥앹쓽�궗�닔', '�씪諛섏쓽 �씤�썝�닔', '�씤�꽩 �씤�썝�닔', '�젅吏��뜕�듃 �씤�썝�닔', '�쟾臾몄쓽 �씤�썝�닔'],
    #       dtype='object')

    # �븘�슂 移쇰읆留� 異붿텧
    result = hospital_LocInfo[['�븫�샇�솕YKIHO肄붾뱶','hosCode','�슂�뼇湲곌��紐�',  '醫낅퀎肄붾뱶紐�', 
    '�떆�룄肄붾뱶紐�',  '�떆援곌뎄肄붾뱶紐�', '�슦�렪踰덊샇', '二쇱냼', '�쟾�솕踰덊샇', '蹂묒썝URL', '媛쒖꽕�씪�옄', 'x醫뚰몴', 'y醫뚰몴']]

    # 移쇰읆 �쁺臾몄쑝濡� 蹂�寃�!
    result.columns = ['YKIHO','hosCode','hosName',  'hosClassName',  'hosCityName',
      'hosCountyName', 'zipCode', 'hosAddress', 'hosPhoneNumber', 'hosUrl', 'hosEstablishment', 
     'Latitude', 'longitude']
    result.to_csv('./hospitalData/hospital_LocInfo01.csv' ,encoding='utf-8-sig')
    # result.columns = ['hosCode','hosName','hosClassCode','hosClassName','hosCityCode','hosCityName'
    # 'hosCountyCode','hosCountyName','zipCode','hosAddress','hosPhoneNumber','hoUrl','hosEstablishment',
    # 'Latitude','longitude']

    return result

# 吏��뿭 �씠由� 諛� pk �깮�꽦�셿猷�!
postHospitalLocInfo =extractLoc()
hostLocResult = postHospitalLocInfo.drop( 'YKIHO', axis=1)
hostLocResult.to_csv('./hospitalData/hospital_LocInfo02.csv' ,encoding='utf-8-sig')
# print(postHospitalLocInfo.columns)

# ---------------------------------------
# 蹂묒썝 �긽�꽭�젙蹂�
# hospital_Info = pd.read_csv('./hospitalData/hospital_Info.csv', encoding='utf-8')
# # subject = ['내과','신경과','정신건강의학과','외과','정형외과','신경외과','흉부외과','성형외과','마취통증의학과',
#      '산부인과','소아청소년과','안과','이비인후과','피부과','비뇨의학과','비뇨기과','영상의학과','방사선종양학과',
#      '병리과','진단검사의학과','결핵과','재활의학과','핵의학과','가정의학과','응급의학과','직업환경의학과','예방의학과',
#      '치과','구강악안면외과','치과보철과','치과교정과','소아치과','치주과','치과보존과','구강내과','영상치의학과',
#      '구강악안면방사선과','구강병리과','예방치과','통합치의학과','한방내과','한방부인과','한방소아과',
#      '한방안·이비인후·피부과','한방안이비인후피부과','한방신경정신과','침구과','한방재활의학과','사상체질과','한방응급']

# print(hospital_Info.columns)
# Index(['�븫�샇�솕YKIHO肄붾뱶', '�슂�뼇湲곌��紐�', '吏꾨즺怨쇰ぉ肄붾뱶', '吏꾨즺怨쇰ぉ肄붾뱶紐�',
#        '怨쇰ぉ蹂� �쟾臾몄쓽�닔', '�꽑�깮吏꾨즺 �쓽�궗�닔'], dtype='object')


# preHospitalInfo = hospital_Info[['�븫�샇�솕YKIHO肄붾뱶', '�슂�뼇湲곌��紐�', '吏꾨즺怨쇰ぉ肄붾뱶', '吏꾨즺怨쇰ぉ肄붾뱶紐�','怨쇰ぉ蹂� �쟾臾몄쓽�닔']]
# preHospitalInfo.columns = ['YKIHO', 'hosName', 'subjectsCode', 'subjectsName','specialists']
# postHospitalLocInfo.sort_values('YKIHO')
# preHospitalInfo.sort_values('YKIHO')



# subject = hospital_Info['吏꾨즺怨쇰ぉ肄붾뱶紐�'].unique().tolist()
# InfoPK = []
# InfoFk = []

# tmpLoc = [[postHospitalLocInfo['YKIHO'].tolist()],[postHospitalLocInfo['hosCode'].tolist()]]
# tmpInfo = [[preHospitalInfo['YKIHO'].tolist()],[preHospitalInfo['subjectsName'].tolist()]]


# preHospitalInfo['hosCode'] = np.nan
# preHospitalInfo['subIndexCode'] = np.nan




# curPos = 0
# for loc in tmpLoc:
#     for i in range(curPos,len(tmpInfo)):
#         if loc[0] != tmpInfo[i][0]:
#             curPos = i
#             break
#         InfoPK.append([loc[1]*100 + subject.index(tmpInfo[i][1])])
#         InfoFk.append([loc[1]])

# preHospitalInfo.to_csv('sample.csv')

# for i , locRow in postHospitalLocInfo.iterrows():    
#     for j ,infoRow  in preHospitalInfo.iterrows():        
#             if locRow['YKIHO'] == infoRow['YKIHO']:
#                 InfoPK.append((locRow['hosCode'] * 100) + subject.index(infoRow['subjectsName']))
#                 InfoFk.append(locRow['hosCode'])

# hospital_Info['hosCode'] = InfoFk
# hospital_Info['subIndexCode'] = InfoFk


# for i,rows in preHospitalInfo.iterrows():    
#     subCode = subject.index(rows['吏꾨즺怨쇰ぉ肄붾뱶紐�'])
    
#     subCodeList.append( subCode[subCode])
    

# preHospitalInfo['subCode'] = subCodeList  # PK
# preHospitalInfo['hosCode'] = tmpHoscode   # FK







