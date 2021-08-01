#%%
from numpy.core.fromnumeric import shape
import pandas as pd
df = pd.read_csv('./preprocess/공공의료기관_기능별_기관_수_2015-2019.csv')
years = pd.DataFrame(df.columns[~df.columns.str.contains('\.')])[1:].reset_index(drop = True)
cities = df[df.columns[0]].drop(range(0,2)).reset_index(drop= True)
result =  pd.DataFrame()
for year in years[0]:
    cityNyear=  pd.DataFrame(cities.copy()).rename(columns= {'시도별(1)':'도시'})
    cityNyear['연도'] = year
    tempDf = df.filter(regex=year)
    cnt =  tempDf[tempDf.columns[::2]]
    percent = tempDf[tempDf.columns[1::2]]
    for i in range(len(percent.columns)):
        tempPercent = pd.DataFrame(percent[percent.columns[i]]).rename(columns = {percent.columns[i]:'퍼센트'})
        tempPercent['기능'] = tempPercent.iloc[0][0] 
        tempPercent = tempPercent.drop(range(0,2)).reset_index(drop=True)
        tempCnt = pd.DataFrame(cnt[cnt.columns[i]]).rename(columns = {cnt.columns[i]:'개수'}).drop(range(0,2)).reset_index(drop=True)
        empMerge = pd.merge(tempPercent,tempCnt,left_index=True,right_index=True)
        empMerge = pd.merge(cityNyear,empMerge,left_index=True,right_index=True)
        result = result.append(empMerge).reset_index(drop=True)

result = result[['도시','연도','기능','개수','퍼센트']]
result
result.to_csv('./postprocess/Post_공공의료기관_기능별_기관_수_2015-2019.csv',encoding='utf-8-sig',index=False)
#%%

cities