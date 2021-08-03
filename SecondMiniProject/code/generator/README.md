# JSON파일

1. seq_length
   - 학습시킬 문장 최대 길이
1. batch_size
   - 배치크기의 사이즈
1. embedding_dim
   - 임베딩 차원 크기
1. rnn_units
   - rnn unit 크기
1. checkpoint_dir
   - RNN 훈련시 생성되는 checkPoint 경로
1. model_Path
   - 생성된 모델 저장 경로
1. Scrapping_Path
   - 크롤링한 소설파일 저장 경로
1. novel_Path & genres
   - 총 장르 수 : 3
     - 0: `romance`
     - 1: `martialArts`
     - 2: `detectiveStory`

# Generation 파일

1. 함수 모듈화

   - [generate_mod.py](./generate_mod.py)
     - 구현한 함수들을 모듈화함
   - 함수들

     1. read_json
        - 생성한 Json파일 읽는 함수
     1. read_text
        - 병합된 텍스트 1개 읽는 함수
     1. read_all_text
        - 스크랩한 소설들 병합
     1. clean_text
        - 텍스트 전처리(클랜징)
     1. indexing

        1. 읽어드린 Text 글자단위로 분해
        1. 분해된 글자 중복제거
        1. 각 값을 char <-> int로 맵핑 (`char2idx` , `idx2char` )
        1. 위 맵핑된 것을 기준으로 Text의 모든 글자에 맵핑 -> (`text_as_int`)

     1. split_input_target
        1. 텍스트를 청크(앞뒤 한개씩 빼고 분할)로 분할해주는 함수
           - Chunck 기준 앞뒤 1글자씩 없애고 생성
        1. `input_text` , `target_text` 생성해줌
     1. build_model

        1. 훈련시킬 베이스 모델 생성
           1. Embedding
           1. LSTM
           1. Dense

     1. loss
        - 손실함수
          - `sparse_categorical_crossentropy` 사용
     1. check_path
        - 모델 저장할 경로여부 판단 및 없다면 디렉토리 생성
     1. model_learning
        - 불러온 Text 및 모델을 사용하여 학습하는 함수
     1. generate_text
        - 학습된 모델을 기반으로 텍스트 생성

1. 메인

   - 아래 2개는 동일함, 단순히 py / ipynb로 만들은 것

     1. [generate_mod.py](./moduled_generator.py)

     1. [moduled_generator.ipynb](./moduled_generator.ipynb)
