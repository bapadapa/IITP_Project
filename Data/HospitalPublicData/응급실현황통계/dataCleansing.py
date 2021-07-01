
# %%
# 필요 라이브러리 impoert
import numpy as py
import pandas as pd

#csv파일 불러오기
path = './'
fileName = '응급실_내원수단_현황_시도별__2014_2019_Kosis.csv'
df =  pd.read_csv( path+fileName )
# 보유 연도 추출
years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"]
# 도시명 추출
cities = df[df.columns[0]].drop(range(0,2)).reset_index(drop=True)
cities

#응급 여부 
emergency =  df.iloc[0][1:].reset_index(drop=True)
emergency

#운송 수단
Vehicle =  df.iloc[1][1:].reset_index(drop=True)
Vehicle

result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['환자'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['응급여부'] = emergency[i]
        tmp['수단'] = Vehicle[i]
        tmp['도시'] = cities
        tmp['연도'] = year
        result = result.append(tmp)
    
result = result[['연도', '도시','응급여부','수단','환자']]
result.to_csv('./Post'+fileName,encoding='utf-8-sig',index=False)
