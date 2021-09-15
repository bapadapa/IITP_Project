#%%
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import seaborn as sns
from sklearn.preprocessing import minmax_scale
from pyarrow import csv
# %%
#%%
# 음식점 등 병합
path ='./localData/cleaned/'
flag = True
for fileN in os.listdir(path):
    readed_file = csv.read_csv(path +fileN).to_pandas()
    readed_file = readed_file.dropna()
    tmp = pd.DataFrame(columns=['시도','년도',readed_file.columns[-1]])
    for city in readed_file.시도.unique():
        for year in readed_file[readed_file.시도 == city].연도.unique():
            tmp= tmp.append(pd.Series(
                [
                    city,
                    year,
                    readed_file[((readed_file.시도 == city) & (readed_file.연도== year))].iloc[:,-1].sum()
                    ] , index = tmp.columns)
                ,ignore_index= True)
    if flag :
        result = tmp.copy()
        flag = False
        continue
    
    result = pd.merge(result, tmp, left_on=['시도','년도'], right_on=['시도','년도'], how='left')
result = result.fillna(0) 

restrant = ['일반음식점','휴게음식점','관광식당',]
bar = ['단란주점', '유흥주점', '외국인전용유흥음식점업',]
result['음식점'] =result[restrant].sum(axis = 1)
result['유흥가'] = result[bar].sum(axis = 1)
result = result.drop(restrant+bar,axis= 1)
result.iloc[:,1:] = result.iloc[:,1:].astype(int)
result.to_csv('semicleaned/local.csv',encoding='utf-8-sig',index=False)
#%% 



#%%

result.to_csv('sample.csv',encoding= 'utf-8-sig',index=False)
#%%
for fp in os.listdir('./localData/cleaned'):
    df = pd.read_csv('./localData/cleaned/'+fp)
    print(df.head(10))
#%%


#%%
flag = True
tmp = pd.DataFrame()
path ='./localData/cleaned/'
for fp in os.listdir(path):    
    print(fp)
#%%
# 범죄 발생지 병합
tmp = pd.DataFrame()
flag = True
for fp in os.listdir('./crime_location'):
    print(fp)
    merged_csv = pd.read_csv('./crime_location/'+fp)
    merged_csv['시도'] = merged_csv['시도'].map({'서울특별시':'서울',
                           '부산광역시':'부산',
                           '대구광역시':'대구',
                           '인천광역시':'인천',
                           '광주광역시':'광주',
                           '대전광역시':'대전',
                           '울산광역시':'울산',
                           '세종특별자치시':'세종',
                           '경기도':'경기',
                           '강원도':'강원',
                           '충청북도':'충북',
                           '충청남도':'충남',
                           '전라북도':'전북',
                           '전라남도':'전남',
                           '경상북도':'경북',
                           '경상남도':'경남',
                           '제주특별자치도':'제주',
                           '서울':'서울',
                           '부산':'부산',
                           '대구':'대구',
                           '인천':'인천',
                           '광주':'광주',
                           '대전':'대전',
                           '울산':'울산',
                           '세종':'세종',
                           '경기':'경기',
                           '강원':'강원',
                           '충북':'충북',
                           '충남':'충남',
                           '전북':'전북',
                           '전남':'전남',
                           '경북':'경북',
                           '경남':'경남',
                           '제주':'제주'})
    if flag :
        tmp = merged_csv
        flag = False
    else:
        tmp = pd.concat([tmp,merged_csv], ignore_index=True)

# result.drop_duplicates()
tmp.drop_duplicates().to_csv('./semicleaned/crime_location.csv',encoding='utf-8-sig',index=False)
print('Done')

# %%
# 모든 데이터 병합
tmp = pd.DataFrame()
flag = True
for fp in os.listdir('./semicleaned'):
    print(fp)
    merged_csv = pd.read_csv('./semicleaned/'+fp)
    merged_csv['시도'] = merged_csv['시도'].map({'서울특별시':'서울',
                           '부산광역시':'부산',
                           '대구광역시':'대구',
                           '인천광역시':'인천',
                           '광주광역시':'광주',
                           '대전광역시':'대전',
                           '울산광역시':'울산',
                           '세종특별자치시':'세종',
                           '경기도':'경기',
                           '강원도':'강원',
                           '충청북도':'충북',
                           '충청남도':'충남',
                           '전라북도':'전북',
                           '전라남도':'전남',
                           '경상북도':'경북',
                           '경상남도':'경남',
                           '제주특별자치도':'제주',
                           '서울':'서울',
                           '부산':'부산',
                           '대구':'대구',
                           '인천':'인천',
                           '광주':'광주',
                           '대전':'대전',
                           '울산':'울산',
                           '세종':'세종',
                           '경기':'경기',
                           '강원':'강원',
                           '충북':'충북',
                           '충남':'충남',
                           '전북':'전북',
                           '전남':'전남',
                           '경북':'경북',
                           '경남':'경남',
                           '제주':'제주',
                           '제주도':'제주'})
    if flag :
        tmp = merged_csv
        flag = False
    else:
        tmp = pd.merge(
            tmp, merged_csv,
            left_on=['년도','시도'],
            right_on=['년도','시도'],
            how='left')
# result.drop_duplicates()

drop_col = ['직무유기',
'직권남용',
'장물',
'수뢰',
'증뢰',
'실화',
'명예',
'권리행사 방해',
'낙태',	
'위증과 증거인멸',
'무고',
'손괴',		
'간통',
'도박과 복표',
'폭력행위등(단체등의구성 활동)',
'혼인빙자간음',		
'통화',
'유가증권인지우표',
'비밀침해',
'신앙',
'문서',
'인장',
'교통방해',
'기타음란행위',
'유가증권·인지·우표',		
'권리행사방해',
'신용업무경매',
'기타 음란행위',	
'신용업무 경매',	
'사기',
'횡령',
'배임',
'범죄소계',
'폭력행위등(손괴강요주거침입등)',
'폭력행위 등 처벌에 관한법률',
'과실치사상',
'업무상 과실치사상',
'일반대 수',
'전문대 수',
'교육대 수',
'산업대 수',
'과실치사상',
'업무상 과실치사상',
'순이동 (명)',
'한국인(남자인구수[명])',
'한국인(여자인구수[명])',
'시도내이동-시군구내 (명)',
'시도내이동-시군구간 전입 (명)',
'시도내이동-시군구간 전출 (명)',
'시도간전입 (명)',
'시도간전출 (명)',
]

tmp = tmp.drop(drop_col,axis = 1).drop_duplicates()
tmp.to_csv('crime_merged.csv',encoding='utf-8-sig',index=False)
print('Done')
#%%
pre2013 = pd.read_csv('crime_location/z_Crime_Location_2013.csv')
post2013 = pd.read_csv('crime_location/z_Crime_Location_2014_.csv')

#%%

tmp[tmp.columns]


#%%
tmp.columns
#%%
# %%
tmp.columns != ['시도','년도']
#%%
def cleaning(x) :
  if str(x).find("-") != -1 :
    return int(str(x).replace("-",'0'))
  return x

df = pd.read_csv('crime_merged.csv')
population = df['한국인(총인구수[명])']
# target data 생성하기
target =['시도',
        '년도',
        '절도',
        '살인',
        '강도',
        '방화',
        '성폭력',
        '협박',
        '공갈',
        '약취와 유인',
        '체포와 감금',
        '폭력행위등(단체등의구성 활동)',
        '주거침입',
        '유기',
        '공무방해',
        '도주와범인은닉']
target_df = df[target]
target_df['폭행및상해'] = df['폭행'].add(df['상해'])
# 모든값 -를 0으로 바꿔주기
for colName in target_df.columns[2:]:
    target_df[colName] = target_df[colName].apply(cleaning)
# 중간값이 String 값으로 들어가는데, 못 찾겠어서 float으로 바꿈
target_df.iloc[:,2:] = target_df.iloc[:,2:].astype(float).div(population,axis = 0)
target_df.to_csv('aa.csv',encoding='utf-8-sig',index=False)
#%%
# 상단에서 병합하여 필요 없다.
# 종속변수 전처리
df = pd.read_csv('crime_merged.csv')
numeric_col = ['시도', '년도',
       '경제활동인구', '비경제활동인구', '취업자', '실업자',
        '1인당 개인소득', '1인당 민간소비', 'PC방', 
       '백화점',  '향정신성의약품 청구건수',
       '경찰청 소속 경찰관 수', '경찰청 인원 1명당 담당 인구', 
       '한국인(인구밀도)', '총전입 (명)', '총전출 (명)', '대학교 수', '종교단체수', '외국인수',
       ]
rate_col = [
       '이혼율','고용률 (%)','실업률 (%)',
       '1인당 지역내총생산', '1인당 지역총소득', '1인당 개인소득','경찰청 인원 1명당 담당 인구','한국인(남녀비율[백분율])',
       '한국인(인구밀도)',]
population = df['한국인(총인구수[명])']

dependent_df = df[numeric_col]
dependent_df['음식점'] = df['일반음식점'].add(df['휴게음식점']).add(df['관광식당'])
dependent_df['유흥가'] = df['단란주점'].add(df['유흥주점']).add(df['외국인전용유흥음식점업'])

# 인구 수로 나눌 값(정규화)들 연산
# dependent_df.iloc[:,2:]  = dependent_df.iloc[:,2:].div(population,axis=0)
# 스케일링 여부는 이후 판단할 것
# dependent_df.iloc[:,2:] = minmax_scale(dependent_df.iloc[:,2:])
# 연산후 다시 병합
dependent_df=  pd.concat([df[rate_col],dependent_df],axis=1)

# dependent_df.to_csv('merged_div_population.csv',encoding='utf-8-sig',index=False)
dependent_df.to_csv('Only_merged_.csv',encoding='utf-8-sig',index=False)
#%
# 확인하기

df = pd.read_csv('crime_merged.csv')
df = df[(df.년도 >= 2009) & (df.년도 <= 2017)] 
df = df.drop(
    ['백화점',
    '경찰청 인원 1명당 담당 인구',
    '한국인(남녀비율[백분율])',
    '한국인(총인구수[명])'],
    axis = 1    
)
div_cols = ['경제활동인구',
'비경제활동인구',
'취업자',
'실업자',
'PC방',
'음식점',
'유흥가',
'향정신성의약품 청구건수',
'경찰청 소속 경찰관 수',
'총전입 (명)',
'총전출 (명)',
'대학교 수',
'종교단체수',
'외국인수',]
df[div_cols] = df[div_cols].div(df['총인구수 (명)'] ,axis = 0)
#%%
#상관계수 보기
df[df.시도 == '서울'].iloc[:,2:].corr().to_csv('tmp_Corr.csv',encoding = 'utf-8-sig')

#%%
font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
sns.heatmap(
    df[df.시도 == '서울'].iloc[:,2:].corr()
)
plt.show()
#%%

#%%
# 지역별 범죄별 corr를 이용하여 Feature Selection
crime_name = df.columns[2:17]
independent_val = df.columns[17:-1] 
df['범죄 합계'] = df[crime_name].sum(axis = 1)
crime_name = crime_name.to_list()+['범죄 합계']
corr_df = pd.DataFrame(columns=['시도','범죄','칼럼리스트'])
for city in df['시도'].unique():
    tmp_df = df[df.시도 == city]
    for crime_ in crime_name:
        tmp_list = []
        for key,value in  (tmp_df[[crime_] + independent_val.to_list()].corr().iloc[0,1:].abs() >= 0.7).to_dict().items():
            if value == True :
                tmp_list += [key]
        if len(tmp_list) < 3:
            continue
        corr_df = corr_df.append(
            pd.Series(
                [city,
                crime_,
                tmp_list],
                index = corr_df.columns
            ),
            ignore_index=True
        )
    
corr_df.to_csv('corr/colList.csv',encoding= 'utf-8-sig',index= False)
#%%

#%%
df = csv.read_csv('./crime_merged.csv').to_pandas()
df = df[(df.년도 >= 2002) & (df.년도 <= 2019)]
crime_name = df.columns[2:17]
df['범죄 합계'] = df[crime_name].sum(axis = 1)
# corr 기준으로 추출된 칼럼 리스트
for i in range(len(corr_df)):
    city = corr_df.iloc[i].시도
    crime = corr_df.iloc[i].범죄
    cols = corr_df.iloc[i].칼럼리스트
    tmp_df = df[(df.시도 == city)]
    tmp_df[
        ['시도','년도',]
        + [crime]
        + cols
        ].to_csv(f'cleaned/{city}_{crime}.csv',encoding= 'utf-8-sig',index= False)

#%%





#%%
for city in df.시도.unique():
    tmp_corr = df[df.시도 == city].iloc[:,2:].corr()
    for  i in tmp_corr.columns:
        tmp_corr.loc[tmp_corr[i].abs() < 0.7,i]= 0
    tmp_corr.to_csv(f'corr/corr_by_crime/sample_corr_{city}.csv',encoding= 'utf-8-sig')
#%%
tmp_corr = df.iloc[:,2:].corr()
for  i in tmp_corr.columns:
    tmp_corr.loc[tmp_corr[i].abs() < 0.7,i]= 0
tmp_corr.to_csv('corr/sample_corr_전국.csv',encoding= 'utf-8-sig')
#%%
















#%%
#%%
merged_div_population = dependent_df.copy()
#%%
Only_merged = dependent_df.copy()
#%%
merged_div_population.columns
#%%
Only_merged
#%%
Only_merged['시도']

#%%
font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
crime_corr = pd.DataFrame()
for colName in target_df.columns[2:]:    
    readed_file = pd.concat([dependent_df,target_df[colName]],axis=1).iloc[:,2:]
    # sns.heatmap(tmp[tmp[colName].isna() == False].corr())
    # plt.show()
    crime_corr[colName] = readed_file[readed_file[colName].isna() == False].corr()[colName][:-1]
    # print(tmp[tmp[colName].isna() == False].corr())
crime_corr.to_csv('crime_corr.csv',encoding='utf-8-sig',index=False) 
#%%
readed_file[readed_file['살인'].isna() == False].corr()['살인']
