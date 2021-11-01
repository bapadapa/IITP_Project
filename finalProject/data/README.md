# 각종 데이터들

1. colNames

   - 여러 칼럼 중 회의를 통하여 필요하다 판단되는 칼럼명들을 기록해둔 디렉토리

1. csv

   - 분석 등을 하면서 필요한 csv들을 모아둔 디렉토리

   1. 최초 수집한 데이터들

      1. 외국인
         - 국내 거주 외국인 데이터
      1. crime_location
         - 지역별 범죄 발생 건수(통합)
      1. crimeData
         - 지역별 범죄 종류별 발생 건수
      1. localData
         - 지역별 음식점, 술집 등의 개수 보유한 데이터
      1. Education
         - 지역별 학력 데이터
      1. Police
         - 지역별 경찰 수 데이터

   1. 정제 후 데이터
      1. semicleaned
         - 최초 수집한 데이터들의 병합형태의 데이터
   1. 최종 데이터
      1. specification
         - 최종 범죄별, 시도별 인덱싱한 데이터
      1. corr
         - 범죄와 각 독립변수간의 상관계수를 추출한 데이터
      1. cleaned
         - 최종 예측 데이터 및 XGBoost의 Hyperparameter을 추출한 데이터

1. geojson

   - 한국 지도를 시각화하기 위한 geojson파일

1. json
   - 데이터 경로 등 자주 사용되는 상수를 정리해놓은 json파일
1. models
   - conv1d 및 Dense를 이용한 cnn 기법으로 생성한 딥러닝 모델
