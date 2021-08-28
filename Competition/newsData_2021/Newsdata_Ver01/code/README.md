# 구현 기술

1. 번역
   - `googleAPI`를 사용.
     - googletrans version = '4.0.0-rc.1'
1. 알림 서비스
   - `Kakao Talk`로 알림 서비스 제작
1. 요약 모델 생성 및 요약
   1. 전처리
      1. nltk
         - stopwords를 사용 할 것인데, 만약 없다면 [공식사이트](http://www.nltk. org/nltk_data/)에 들어가서 설치 후 운영체제에 맞는 위치에 이동시킬것.
           - ex ) C:\Users\사용자명\Anaconda3\envs\환경명\nltk_data\corpora\stopwords
             - 중간 경로가 없다면 생성해야함
      1. lxml을 사용하려면 추가 설치해야함
         - `pip3 install lxml`
