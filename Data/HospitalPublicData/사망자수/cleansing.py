"""
공공 데이터 전처리
사망원인_성_시도별_사망자수_1983_2019.csv
"""
#%%
import pandas as pd
import numpy as np

def cleansing(df): 
    result = pd.DataFrame()
    for year in years :
        tmp = pd.DataFrame()
        tmp['사망자수'] = (df[year+' 년'])
        tmp['연도'] = year        
        tmp = tmp.join(df[df.columns[:3]],how='inner')
        result = result.append(tmp)
    return(result)

fileName = '사망원인_성_시도별_사망자수_1983_2019.csv'
# df = pd.read_csv('./'+fileName)
df = pd.read_csv(fileName)
df.drop(['항목'],axis = 1 , inplace= True)
years = [i[:4] for i in df.columns[4:]]

result = cleansing(df)
result = result[['연도','시도별','사망자수','사망원인별','성별']]
result.to_csv('./Post'+fileName,encoding='utf-8-sig',index= False)


