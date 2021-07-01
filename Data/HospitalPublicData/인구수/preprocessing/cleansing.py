"""
전처리
행정구역_시군구_별__성별_인구수_1992_2020_Kosis.csv
"""
#%%
import pandas as pd
fileName = '행정구역_시군구_별__성별_인구수_1992_2020_Kosis.csv'
df = pd.read_csv('./'+fileName)
def cleansing(df):
    result = pd.DataFrame()
    for year in years[years.columns[0]]:
        tmp = df.filter(regex=year).drop(0)
        men = pd.DataFrame()
        women = pd.DataFrame()
        men['인구수'] = tmp[tmp.columns[0]]
        men['성별'] = 'M'
        men['도시'] = cities
        women['인구수'] = tmp[tmp.columns[1]]
        women['성별'] = 'W'
        women['도시'] = cities
        population = men.append(women)[::-1]
        population
        # 추출한 것 합치기
        tmp = population[population.columns[::-1]]
        tmp['연도'] = year
        result = result.append(tmp)
    
    return(result)

# 연도 추출
years = pd.DataFrame(df.columns[~df.columns.str.contains('\\.')]).drop(0).reset_index(drop = True)
years.columns = ['연도']
# 성별 추출
gender = pd.DataFrame(df.iloc[0], ).reset_index(drop = True)
gender.columns = [gender[0][0]]
gender.drop(0)

# 도시 추출
cities = pd.DataFrame(df[df.columns[0]].drop(0))
cities.columns = ['도시']

#최종 도출 CSV
result = cleansing(df).sort_values(by = ['연도','도시'],axis =0).reset_index(drop = True)
result = result[['연도','도시','성별','인구수']]
result.to_csv('./Post'+fileName,encoding='utf-8-sig',index= False)
    