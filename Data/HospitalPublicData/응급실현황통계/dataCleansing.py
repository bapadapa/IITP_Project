
# %%
# 필요 라이브러리 impoert
import numpy as py
import pandas as pd
import os 

# %%
#csv파일 불러오기
path = './'
fileName = '응급실_내원수단_현황_시도별__2014_2019_Kosis.csv'
df =  pd.read_csv( path+fileName )
# 보유 연도 추출
year = df.columns
year = pd.DataFrame(year[~year.str.contains('\.')])[1:]
year.columns = ["연도"]
# print()





# %%
year.reset_index(drop = False, inplace = True)
year

# %%
