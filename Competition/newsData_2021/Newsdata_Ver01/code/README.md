# 구현 기술

1. 번역
   - `googleAPI`를 사용.
     - googletrans version = '4.0.0-rc.1'
1. 알림 서비스
   - `Kakao Talk`로 알림 서비스 제작
1. 요약 모델 생성 및 요약

   1. 전처리
      1. 위험 및 안전 단어를 분류
         1. 위험에 관련된 키워드로 크롤링한 값들은 `0`으로 변환
         1. 안전에 관련된 키워드로 크롤링한 값들은 `1`으로 변환
      1. 불용어 등 불필요 String 삭제
         1. nltk
            - stopwords를 사용 할 것인데, 만약 없다면 [공식사이트](http://www.nltk. org/nltk_data/) 에 들어가서 설치 후 운영체제에 맞는 위치에 이동시킬것.
              - ex ) C:\Users\사용자명\Anaconda3\envs\환경명\nltk_data\corpora\stopwords
                - 중간 경로가 없다면 생성해야함
         1. 불용어 제거
            1. re.sub , BeautifulSoup, 축약사전, stopword 등을 이용하여 제거함
               1. BeautifulSoup(newString, "lxml").text을 사용하려면 추가 설치해야함
                  - `pip3 install lxml`
      1. tokenize
         1. `key : value`로 `문자 데이터`를 `Dict`로 변환시켜줌.
         1. 빈도수가 적은 (코드 기준 3개 이하)는 제거해줌
         1. tokenize가 완료되면, `Sentence`를 `Index값` 즉 `Sequences`로 만들어줌
         1. 각 `Sequence`의 길이가 다르기때문에 동일한 길이로 맞추기 위해 `Padding`을 해줌
      1. Train Test 분리
         1. sklearn의 train_test_split을 이용하여 분리시켜줌
   1. 모델 생성 및 훈련

      1. 문맥을 이해하는게 중요하기 때문에 `LSTM`을 사용하여 구현
      1. `GRU & LSTM`의 조합으로 초기에 구현하였지만, `LSTM만 사용` 한 것이 더 좋은 결과를 얻어 `GRU는 탈락`시킴
      1. `Sequential` 과 `Concatenate`를 동일한 조건에서 훈련시킨 결과, Sequential로 구현한 것이 더 좋은 결과를 얻어 `Sequential 채택`
      1. dropout을 처음에는 0.4로 하였는데, overfitting이 생각보다 많이 발생하여 0.5로 변경
      1. model 구성

         - ```python

               model = Sequential([
                Embedding(vocab_size, 256),
                LSTM(
                   512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.5, recurrent_dropout=0.5
                   ),
                LSTM(
                   512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.5,recurrent_dropout=0.5
                   ),
                LSTM(
                   512,kernel_initializer='he_uniform',dropout=.5,recurrent_dropout=0.5
                   ),
                Dense(256, activation='relu',kernel_initializer='he_uniform'),
                Dropout(.5),
                Dense(128, activation='relu',kernel_initializer='he_uniform'),
                Dropout(.5),
                Dense(128, activation='relu',kernel_initializer='he_uniform'),
                Dense(1, activation='sigmoid')
            ])
           ```

      1. Model Compile

         1. Optimizer
            1. `Adam` 과 `RMSprop`를 테스트해본 결과 RMSprop가 더 좋은 결과값을 주어 `RMSprop채택`
         1. Loss
            1. 위험 및 안전 2개의 결과가 필요하기 때문에 `BinaryCrossentropy`를 사용

      1. Model Fitting
         1. callback
            1. EarlyStopping
               - 최적의 시간 및 결과를 얻기 위해 사용
