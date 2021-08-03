#%%
import tensorflow as tf
import numpy as np
import os 
import json

#파일 가져오기
# Json 파일 읽기
with open("config.json", "r", encoding = 'utf-8') as common:
    config = json.load(common)

file_path = config['novel_Path'][0]+'.txt'
text = open(file_path,'rb').read().decode()

# txt 단어 단위로 중복제거 및 인덱싱
vocab = sorted(set(text))
# 중복 제거된 단어에 index 만들어주기
char2idx = {word : index for index ,word in enumerate(vocab)}
# 인덱싱 사전 생성
idx2char = np.array((vocab))

# 중복 제거하여 인덱싱 된 벡터를 기준으로
# 전체 텍스트 인덱싱
text_as_int = np.array([char2idx[c] for c in text])

# echoch 당 문장 길이
# -----------텍스트의 모든 단어 읽어서 가장 긴 값을 삽입해보자
# -----Json으로 뺄것

# training Sample/Target 생성
# numpy -> tensor 형변환이라고 생각하는게 편함
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

# 청크파일 만들기 (즉 훈련 셈플등을 구하기)
sequences =char_dataset.batch(config['seq_length']+1 , drop_remainder = True)

# 텍스트를 청크(앞뒤 한개씩 빼고 분할)로 분할해주는 함수
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text , target_text

dataset = sequences.map(split_input_target)

# 버퍼사이즈 설정
BUFFER_SIZE = len(text_as_int) * 2
# BUFFER_SIZE개로 이루어진 버퍼로 임의의 샘플을 뽑는다.
# 그것을 다시 BATCH_SIZE로 분할한다.
dataset = dataset.shuffle(BUFFER_SIZE).batch(config['batch_size'], drop_remainder= True)

# RNN 유닛 개수
rnn_units= 1024

# Embedding, LSTM, DENSE를 이용하여 모델 생성하는 함수
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    return tf.keras.Sequential([
        tf.keras.layers.Embedding(
            vocab_size, embedding_dim, batch_input_shape = [batch_size, None]),
        tf.keras.layers.LSTM(
            rnn_units, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),
            #rnn_units, return_sequences=True, stateful=True, recurrent_initializer='glorot_normal'),
        tf.keras.layers.Dense(
            vocab_size)            
    ])

model = build_model(
    vocab_size = len(vocab),
    embedding_dim = config['embedding_dim'],
    rnn_units = rnn_units,
    batch_size = config['batch_size']
)

def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(
      labels, logits, from_logits=True)

model.compile(optimizer='adam', loss=loss)

# 체크파일 명
checkpoint_prefix = os.path.join(config['checkpoint_dir']+config['genres'][0], "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath = checkpoint_prefix,
    save_weights_only = True)

EPOCHS= 10

model.fit(dataset, epochs=EPOCHS, callbacks=[checkpoint_callback])

model = build_model(
    vocab_size = len(vocab),
    embedding_dim = config['embedding_dim'],
    rnn_units = rnn_units,
    batch_size = 1
)

model.load_weights(tf.train.latest_checkpoint(config['checkpoint_dir']+config['genres'][0]))

model.build(tf.TensorShape([1, None]))

#%%
model.summary()
#%%

def generate_text2(temperature,model, start_string):
  # 평가 단계 (학습된 모델을 사용하여 텍스트 생성)

  # 생성할 문자의 수
  num_generate = 500

  # 시작 문자열을 숫자로 변환(벡터화)
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  # 결과를 저장할 빈 문자열
  text_generated = []

  # 온도가 낮으면 더 예측 가능한 텍스트가 됩니다.
  # 온도가 높으면 더 의외의 텍스트가 됩니다.
  # 최적의 세팅을 찾기 위한 실험

  # 여기에서 배치 크기 == 1
  model.reset_states()
  for i in range(num_generate):
      predictions = model(input_eval)
      # 배치 차원 제거
      predictions = tf.squeeze(predictions, 0)

      # 범주형 분포를 사용하여 모델에서 리턴한 단어 예측
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      # 예측된 단어를 다음 입력으로 모델에 전달
      # 이전 은닉 상태와 함께
      input_eval = tf.expand_dims([predicted_id], 0)

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))

for i in np.linspace(0.,1.,10): 
  print('\n\n'+f'\n\ntemp = {i}' ,generate_text2(i,model, start_string=u"도깨비 "))

#%%
# len(text_as_int)
text_as_int.size
len(sequences)
len(char_dataset)
len(text_as_int)