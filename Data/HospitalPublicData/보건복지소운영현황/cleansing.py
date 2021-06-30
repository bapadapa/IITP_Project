"""
공공 데이터 전처리

"""
#%%
# import
import pandas as pd
import numpy as np
import os 

# %%

# 보건소_인력현황시도별_1994_2011_Kosis.csv
def cleansing(df):
    result = pd.DataFrame()
    for i in year[0]:
        tmp = file01.filter(regex= i)
        tmp.columns = tmp.iloc[0]
        tmp['연도'] = i
        tmp['도시'] = citys
        tmp = tmp.drop(0)
        result = result.append(tmp)
    return (result)

data = ('보건소_인력현황시도별_1994_2011_Kosis.csv',
'보건소_인력현황시도별_2012_2019_Kosis.csv')
file01 = pd.read_csv('./'+data[0])


# 도시명 추출
citys = file01[file01.columns[0]].reset_index(drop = True)

# 보유 연도 추출
year = file01.columns[:]
year = pd.DataFrame(year[(~year.str.contains('\.'))]).drop(0)
# 전처리
result = cleansing(file01)
result.reset_index(drop=True)
result[result.columns[-6:-4].to_list()+
                result.columns[:-6].to_list()+                
                result.columns[-4:].to_list()].to_csv('./Post_'+data[0],encoding='utf-8-sig',index= False)
# %%
file01
# %%


