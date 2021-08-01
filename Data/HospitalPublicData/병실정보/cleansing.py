#%%
# import
from typing import ValuesView
import pandas as pd
import numpy as np

# %%
## 함수 생성
def clean(tmp,year):
    temp = pd.DataFrame()
    for i in range(len(tmp)):
        tmp2 = pd.DataFrame(tmp.iloc[i][3:].reset_index(drop=True))
        tmp2.columns = ['개수']
        tmp2['도시'] = citys
        tmp2['병실종류'] = tmp.iloc[i][0]
        tmp2['병실_병상수'] = tmp.iloc[i][2][:3]
        tmp2['연도'] = year
        temp = temp.append(tmp2)
    return temp
# %%
df = pd.read_csv('./시도별_병실_현황_2011_2019.csv')
# 도시명 추출
citys = df[df.columns[0]][3:,].reset_index(drop = True)
year = df.columns[:]
# 보유 연도 추출
year = pd.DataFrame(year[(~year.str.contains('\.'))]).drop(0)

result = pd.DataFrame()
# 람다식 어떻게 사용했는지 기억해 내자
for i in year[0]:
    tmp = df.filter(regex= i).T
    result = result.append(clean(tmp,i))
result.reset_index(drop=True)
result = result[['연도','도시','병실종류','병실_병상수','개수']]
result.to_csv('./Post_시도별_병실_현황_2011_2019.csv',encoding='utf-8-sig',index= False)


# %%
import pandas as pd
df = pd.read_csv('./postprocess/Post_시도별_병실_현황_2011_2019.csv')
result =df[df.병실_병상수 == '병실수']
result.rename(columns = {'개수':'병실수'},inplace=True)
result = result[['연도','도시','병실종류','병실수']].reset_index(drop=True)
result['병상수'] = pd.DataFrame(df[df.병실_병상수 == '병상수']['개수']).reset_index(drop= True)
# result.to_csv('./Post2_시도별_병실_현황_2011_2019.csv',encoding='utf-8-sig',index= False)
result.shape

#%%
ValuesView
