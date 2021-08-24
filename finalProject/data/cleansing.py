#%%
from numpy.core.fromnumeric import shape
from numpy.core.numeric import NaN
import pandas as pd
import os
import re
# path = './localData/술집/' 
# list = os.listdir(path)
# df = pd.read_csv(path+list[0],encoding = 'ansi')

#%%

path = './localData/음식점,카페,편의점/휴게음식점.csv'
df = pd.read_csv(path,encoding = 'ansi')

path = './localData/음식점,카페,편의점/휴게음식점.csv'
df = pd.read_csv(path,encoding = 'ansi')

df = df[['인허가일자','폐업일자','소재지전체주소','도로명전체주소']]

df['인허가일자'] = df['인허가일자']//1e+4
df['폐업일자'] = df['폐업일자']//1e+4
df = df.fillna(value = {'폐업일자' : 2021})

df = df[df['폐업일자'] >= 2000]
df = df[df['인허가일자'] >= 1500]
df.loc[df['인허가일자'] <= 2000,'인허가일자']  = 2000
df = df.sort_values(by = '인허가일자')

for i in  df[df['소재지전체주소'].isna()].index:
    df['소재지전체주소'][i] = df['도로명전체주소'][i]
tmp = df[['인허가일자','폐업일자']]
tmp['시도'] = df['소재지전체주소'].str.split(' ').str[0]
tmp['시군구'] = df['소재지전체주소'].str.split(' ').str[1]

# result.to_csv('./aa.csv',index=False,encoding='utf-8-sig')
df = tmp.reset_index(drop=True)
result = pd.DataFrame(columns=['시도','시군구','연도','휴게음식점'])
for city in df['시도'].unique():
    tmp_city = df [ df['시도'] == city]
    for county in tmp_city[tmp_city['시도'] == city].시군구.unique():
        tmp = tmp_city[tmp_city['시군구'] == county]
        for i in range(2000,2022):
            condition = ((i - tmp['인허가일자']) >= 0) & ((tmp['폐업일자'] - i) >= 0)
            data = tmp[condition] 
            result.loc[result.shape[0]] = [
                city,
                county,
                i,
                len(data),                
                ]
                
result.to_csv('./localData/음식점,카페,편의점/휴게음식점_cleaned.csv',index=False,encoding='utf-8-sig')

#%%
# 백화점내 음식점 중복 제거하여 추출
path = './휴게음식점.csv'
df = pd.read_csv(path,encoding = 'utf-8')
def removeDuplicate(df):
    df = df[df['위생업태명'] == '백화점']
    df = df[['인허가일자','폐업일자','소재지우편번호','소재지전체주소','도로명전체주소']]
    df['인허가일자'] = df['인허가일자']//1e+4
    df['폐업일자'] = df['폐업일자']//1e+4
    df = df.fillna(value = {'폐업일자' : 2021})
    df = df[df['폐업일자'] >= 2000]
    df = df[df['인허가일자'] >= 1500]
    df.loc[df['인허가일자'] <= 2000,'인허가일자']  = 2000
    df = df.sort_values(by = '인허가일자')

    for i in  df[df['소재지전체주소'].isna()].index:
        df['소재지전체주소'][i] = df['도로명전체주소'][i]
    for i in df['소재지우편번호'].unique():
        df.loc[df['소재지우편번호'] == i,'인허가일자'] = df[df['소재지우편번호'] == i].인허가일자.min()
        df.loc[df['소재지우편번호'] == i,'폐업일자'] = df[df['소재지우편번호'] == i].폐업일자.max()
        df = df.drop_duplicates(['소재지우편번호'])
    tmp = df[['인허가일자','폐업일자']]
    tmp['시도'] = df['소재지전체주소'].str.split(' ').str[0]
    tmp['시군구'] = df['소재지전체주소'].str.split(' ').str[1]
    df = tmp.reset_index(drop=True)
    result = pd.DataFrame(columns=['시도','시군구','연도','휴게음식점'])
    for city in df['시도'].unique():
        tmp_city = df [ df['시도'] == city]
        for county in tmp_city[tmp_city['시도'] == city].시군구.unique():
            tmp = tmp_city[tmp_city['시군구'] == county]
            for i in range(2000,2022):
                condition = ((i - tmp['인허가일자']) >= 0) & ((tmp['폐업일자'] - i) >= 0)
                data = tmp[condition] 
                result.loc[result.shape[0]] = [
                    city,
                    county,
                    i,
                    len(data),                
                    ]
    result.to_csv('./localData/음식점,카페,편의점/백화점_cleaned.csv',index=False,encoding='utf-8-sig')
    return tmp.reset_index(drop=True)
removeDuplicate(df)










#%%
tmp = df[df['시도'] == '강원도']
tmp = tmp[df['시군구'] =='횡성군'].reset_index(drop=True)
tmp[tmp['인허가일자']== 2000].인허가일자.count()
tmp
# tmp.to_csv('./aa.csv',index=False,encoding='utf-8-sig')


#%%
tmp.loc[tmp['인허가일자']== 2000,'인허가일자'] = 2001
#%%
print(tmp['인허가일자'] - tmp['폐업일자'])
#%%
for i in range(2000,2022):
    result.loc[result.shape[0]] = [i,
    tmp[tmp['인허가일자']== 2000].인허가일자.count(),
    '강원도',
    '횡성']
    tmp.loc[tmp['인허가일자']== i,'인허가일자'] = i+1

    
#%%

result
#%%

for i in range(2000,2022):
    condition = ((i - tmp['인허가일자']) >= 0) & ((tmp['폐업일자'] - i) >= 0)
    data = tmp[condition]
    result.loc[result.shape[0]] = [
        i,
        len(data),
        '강원도',
        '횡성']
result
#%%
tmp
#%%

result.loc[result.shape[0]] = [2000,
    tmp[tmp['인허가일자']== 2000].인허가일자.count(),
    '강원도',
    '횡성']
    
result


