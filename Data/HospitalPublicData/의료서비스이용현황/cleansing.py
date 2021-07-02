#%%
import pandas as pd
fileName = '연도별_상병별_1일_외래환자수_1990_2016_Kosis.csv'
path = './'
df = pd.read_csv(path+fileName)

years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"] 
# 상병분류별
Classification = pd.DataFrame(df[df.columns[0]])
result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['환자수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['싱뱡분류별'] = Classification[Classification.columns[0]]
        tmp['연도'] = year
        result = result.append(tmp)
    
result[result.columns[::-1]].to_csv(path+'post_'+fileName , encoding='utf-8-sig',index=False)
# %%
import pandas as pd
fileName = '연도별_상병별_퇴원환자_평균재원일수_1990_2016_Kosis.csv'
path = './'
df = pd.read_csv(path+fileName)

years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"] 
# 상병분류별
Classification = pd.DataFrame(df[df.columns[0]])
result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['일수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['싱뱡분류별'] = Classification[Classification.columns[0]]
        tmp['연도'] = year
        result = result.append(tmp)
    
result[result.columns[::-1]].to_csv(path+'post_'+fileName , encoding='utf-8-sig',index=False)
#%%
import pandas as pd
# fileName = '연도별_의료기관종별_1개월간_퇴원환자수_1990_2016_Kosis.csv'
# fileName = '연도별_의료기관종별_1일_외래환자수_1990_2016_Kosis.csv'
fileName = '연도별_성·연령구간별_1개월간_퇴원환자수_2002_2016_Kosis.csv'
path = './'
df = pd.read_csv(path+fileName)

years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"] 
# 상병분류별
Classification = pd.DataFrame(df[df.columns[0]])
result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['환자수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['의료기관종별'] = Classification[Classification.columns[0]]
        tmp['연도'] = year
        result = result.append(tmp)
    
result[result.columns[::-1]].to_csv(path+'post_'+fileName , encoding='utf-8-sig',index=False)

#%%
import pandas as pd
# fileName = '연도별_성·연령구간별_1개월간_퇴원환자수_2002_2016_Kosis.csv'
# fileName = '연도별_성·연령구간별_1일_외래환자_수진율_2002_2016_Kosis.csv'
fileName = '연도별_성·연령구간별_퇴원율_2002_2016_Kosis.csv'

path = './'
df = pd.read_csv(path+fileName)

years = df.columns
years = pd.DataFrame(years[~years.str.contains('\.')])[1:].reset_index(drop = True)
years.columns = ["연도"] 
age = df[df.columns[0]][1:].reset_index(drop=True)
age[0] = '총계'
sex = df.iloc[0][1:]
result = pd.DataFrame()
for year in years[years.columns[0]]:
    temp = df.filter(regex=year)
    for i in range(len(temp.columns)):
        tmp = pd.DataFrame()    
        tmp['환자수'] = temp[temp.columns[i]][2:].reset_index(drop = True)
        tmp['성별'] = sex[i]
        tmp['나이'] = age  
        tmp['연도'] = year
        result = result.append(tmp)
result[result.columns[::-1]].to_csv(path+'post_'+fileName , encoding='utf-8-sig',index=False)
# %%
