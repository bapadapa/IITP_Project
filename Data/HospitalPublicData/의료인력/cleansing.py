#%% 
# 병상병실수-03-20-kosis.csv
import pandas as pd
fileName = '병상병실수-03-20-kosis.csv'
path = './'

df = pd.read_csv(path+fileName )
years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"]
# 도시명 추출
cities = df[df.columns[0]].drop(range(0,2)).reset_index(drop=True)

count = df.iloc[0].reset_index(drop=True).drop(0)

result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['병상수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['조사'] = count.iloc[i]
        tmp['도시'] = cities
        tmp['연도'] = year
        result = result.append(tmp)
result[result.columns[::-1]].to_csv(path+'post_'+fileName,encoding = 'utf-8-sig',index=False)
# %%
# 의료기관수-kosis-07~20.csv
import pandas as pd
fileName = '의료기관수-kosis-07~20.csv'
path = './'
df = pd.read_csv(path+fileName )
years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"]
# 도시명 추출
cities = df[df.columns[0]].drop(range(0,2)).reset_index(drop=True)

count = df.iloc[0].reset_index(drop=True).drop(0)

result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['종사자수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['조사자'] = count.iloc[i]
        tmp['도시'] = cities
        tmp['연도'] = year
        result = result.append(tmp)
result[result.columns[::-1]].to_csv(path+'post_'+fileName,encoding = 'utf-8-sig',index=False)
#%%
# 의사수-2007-2019-kosis.csv
import pandas as pd
fileName = '의사수-2007-2019-kosis.csv'
path = './'
df = pd.read_csv(path+fileName )
years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"]
# 도시명 추출
cities = df[df.columns[0]].drop(range(0,2)).reset_index(drop=True)

count = df.iloc[0].reset_index(drop=True).drop(0)

result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['종사자수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['조사자'] = count.iloc[i]
        tmp['도시'] = cities
        tmp['연도'] = year
        result = result.append(tmp)
result[result.columns[::-1]].to_csv(path+'post_'+fileName,encoding = 'utf-8-sig',index=False)