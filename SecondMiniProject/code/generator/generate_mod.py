import json
import tensorflow as tf
from tensorflow.python.keras import activations
from tensorflow.python.keras.models import load_model
import os
import re
import numpy as np
from pytesseract import *
from PIL import Image
import glob
import os
import sys
from functools import partial

# image -> txt
def ocr(file_dir , lang = 'kor'):
    # images_URL = glob.glob("C:/mini_project_2/1레벨 초월자 001-025/*.gif")
    images_URL = glob.glob(file_dir)
    result = ''
    for i in images_URL:
        result = result + pytesseract.image_to_string(Image.open(i),lang = lang)
    sys.stdout = open('ocr_result.txt', 'w')
    print(result)
    sys.stdout.close()
    return result
    
# Json 파일 읽어오기
def read_json(jsonPath = "config.json" ,mod = 'r',encoding ='utf-8'):
    with open(jsonPath, mod, encoding = encoding) as common:
        config = json.load(common)
    return config

# 소설책 읽어오기
def read_text(file_path):    
    try : 
        with open(file_path,'rb') as common:
            text = common.read().decode(encoding='utf-8')
    except : 
        with open(file_path,'rb') as common:
            text = common.read().decode(encoding='ansi')
    return text
    

# 디렉토니 내부의 모든 소설책 읽어오기
def read_all_text(config,genre):    
    dir_path = config['novel_Path'] + genre    
    novel_list = os.listdir(dir_path)
    text = ""    
    for novel in novel_list:
        
        try : 
            try :
                with open(dir_path+'/'+novel ,'rb') as common:
                    text += common.read().decode(encoding='ansi')             
            except :
                
                with open(dir_path+'/'+novel ,'rb') as common:
                    text += common.read().decode(encoding='utf-8')  
        except :
            print(novel)
            pass    
    text = clean_text(text)
    try :
        with open(dir_path+'.txt' ,'w' , encoding='utf-8') as txt:
            txt.write(text)            
    except :
        with open(dir_path+'.txt' ,'w' , encoding='ansi') as txt:
            txt.write(text)            

    # 합쳐진 텍스트 정제 후 반환
    return text


# 읽어드린 텍스트파일 정제
def clean_text(text):    
    result = re.sub('[^a-zA-Z0-9가-힣\.\?\!\s]', '', text)
    result = re.sub(' \r\n', '  ', result)
    result = re.sub('\r\n ', '  ', result)
    result = re.sub(' +', ' ', result)    
    result = re.sub('\.+','.',result)    
    result = re.sub('\?+','?',result)  
    result = re.sub('(\r\n)+', '\r\n', result)
    # result = re.sub('\n ', '', result)
    # result = re.sub('\n', '\n ', result)
    return result

def indexing(text):
    # txt 단어 단위로 중복제거 및 인덱싱
    vocab = sorted(set(text))
    # 중복 제거된 단어에 index 만들어주기
    char2idx = {word : index for index ,word in enumerate(vocab)}
    # 인덱싱 사전 생성
    idx2char = np.array((vocab))
    # 중복 제거하여 인덱싱 된 벡터를 기준으로
    # 전체 텍스트 인덱싱
    text_as_int = np.array([char2idx[c] for c in text])

    return vocab,char2idx,idx2char,text_as_int


# 텍스트를 청크(앞뒤 한개씩 빼고 분할)로 분할해주는 함수
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text , target_text

# Embedding, LSTM, DENSE를 이용하여 모델 생성하는 함수
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    return tf.keras.Sequential([
        tf.keras.layers.Embedding(
            vocab_size, embedding_dim, batch_input_shape = [batch_size, None]),
        tf.keras.layers.LSTM(
            rnn_units, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform' ),
            #rnn_units, return_sequences=True, stateful=True, recurrent_initializer='glorot_normal'),
        tf.keras.layers.Dense(
            rnn_units , activation=partial(tf.nn.leaky_relu, alpha=0.01)),
        # tf.keras.layers.Dense(
        #     rnn_units , activation='relu'),
        tf.keras.layers.Dense(            
            vocab_size)            
    ])
    
# 다중 분류 손실 함수
# integer type 클래스 -> one-hot encoding하지 않고 정수 형태로 label(y)을 넣어줌
# 한 샘플에 여러 클래스가 있거나 label이 soft 확률일 경우 사용
def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(
      labels, logits, from_logits=True)

# Path 에 디렉토리가 없으면 생성해줌
def check_path(Path):
    if not os.path.isdir(Path):
        os.mkdir(Path)

# 딥러닝을 통해 모델 생성
def model_learning(config ,vocab ,dataset ,genre_Index):
    model = build_model(
    vocab_size = len(vocab),
    embedding_dim = config['embedding_dim'],
    rnn_units = config['rnn_units'],
    batch_size = config['batch_size']
    )
    model.compile(optimizer='adam', loss=loss)

    checkPoint_Path = config['checkpoint_dir']+config['genres'][genre_Index]

    check_path(checkPoint_Path)
    checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
        # 체크포인트 파일 경로 및 체크파일 명
        filepath = os.path.join(checkPoint_Path, "ckpt_{epoch}"),
        save_weights_only = True)
    # save_weights_only
    # - True, False
    # - True인 경우, 모델의 weights만 저장됩니다.
    # - False인 경우, 모델 레이어 및 weights 모두 저장됩니다.

    model.fit(dataset, epochs=config['EPOCHS'], callbacks=[checkpoint_callback])

    model = build_model(
        vocab_size = len(vocab),
        embedding_dim = config['embedding_dim'],
        rnn_units = config['rnn_units'],
        batch_size = 1
    )

    model.load_weights(tf.train.latest_checkpoint(config['checkpoint_dir']+config['genres'][genre_Index]))

    model.build(tf.TensorShape([1, None]))

    # 경로에 디렉토리 없을시 생성 후 저장
    check_path(config['model_Path'])
    model_path = config['model_Path'] + config['genres'][genre_Index]
    
    model.save(f'{model_path}.h5')

    return model

# 생성된 모델로 문장 생성하기
def generate_text( model_index, start_string,num_generate = 1000,temperature = 0.7):    
    
    #파일 가져오기
    # Json 파일 및 소설 가져오기 읽기
    config = read_json()
    text = read_text(config['novel_Path']+config['genres'][model_index]+'.txt')

    # 인덱싱 사전 생성 및 모든 텍스트 맵핑시킴
    vocab, char2idx, idx2char , text_as_int  = indexing(text)

    model_Path = config['model_Path'] + config['genres'][model_index]
    model = load_model(f'{model_Path}.h5')

    # 평가 단계 (학습된 모델을 사용하여 텍스트 생성)
  
    # 시작 문자열을 숫자로 변환(벡터화)
    input_eval = [char2idx[s] for s in start_string]  
    input_eval = tf.expand_dims(input_eval, 0)
  
    # 결과를 저장할 빈 문자열
    text_generated = []
    # 여기에서 배치 크기 == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # 배치 차원 제거
        predictions = tf.squeeze(predictions, 0)
        
        # 범주형 분포를 사용하여 모델에서 리턴한 단어 예측      
        # 온도가 낮으면 더 예측 가능한 텍스트가 됩니다.
        # 온도가 높으면 더 의외의 텍스트가 됩니다.
        # 최적의 세팅을 찾기 위한 실험
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
  
        # 예측된 단어를 다음 입력으로 모델에 전달
        # 이전 은닉 상태와 함께
        input_eval = tf.expand_dims([predicted_id], 0)
  
        text_generated.append(idx2char[predicted_id])
    
    return clean_text(start_string + ''.join(text_generated))