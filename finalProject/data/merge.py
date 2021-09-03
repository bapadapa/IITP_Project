#%%
import pandas as pd
import os
# %%

#%%
for fp in os.listdir('./localData/cleaned'):
    df = pd.read_csv('./localData/cleaned/'+fp)
    print(df.head(10))
#%%
flag = True
result = pd.DataFrame()
for fp in os.listdir('./localData/cleaned'):
    df = pd.read_csv('./localData/cleaned/'+fp)
    tmp_merged = pd.DataFrame()
    for city in df['시도'].unique():
        tmp = pd.DataFrame(columns=['연도','시도',df.columns[-1]])
        for year in df['연도'].unique():
            tmp = tmp.append(
                {
                '연도' : year,
                '시도' : city,
                df.columns[-1] : df[(df['시도'] == city) & (df['연도'] == year)].iloc[:,[-1]].sum()[-1]
                },ignore_index=True)
        tmp_merged = tmp_merged.append(tmp,ignore_index=True)
    if flag :
        result = tmp_merged
        flag = False
    else:
        result = pd.merge(result, tmp_merged, left_on=['연도','시도'], right_on=['연도','시도'], how='left')

result.to_csv('semicleaned/local.csv',encoding='utf-8-sig',index=False)
# %%
result = pd.DataFrame()
flag = True
for fp in os.listdir('./semicleaned'):
    merged_csv = pd.read_csv('./semicleaned/'+fp)
    if flag :
        result = merged_csv
        flag = False
    else:
        result = pd.merge(result, merged_csv, left_on=['년도','시도'], right_on=['년도','시도'], how='left')
result.drop_duplicates().to_csv('crime_merged.csv',encoding='utf-8-sig',index=False)
#%%
result.shape