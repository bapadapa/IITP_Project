#%%
# 생성한 모듈 경로
import generate_mod
# 그 외의 모듈들
import tensorflow as tf

#파일 가져오기
# Json 파일 및 소설 가져오기 읽기
config = generate_mod.read_json()
text = generate_mod.read_all_text(config,config['genres'][1])

# 인덱싱 사전 생성 및 모든 텍스트 맵핑시킴
vocab, char2idx, idx2char , text_as_int  = generate_mod.indexing(text)

# training Sample/Target 생성
# numpy -> tensor 형변환이라고 생각하는게 편함
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

# 청크파일 만들기 (즉 훈련 셈플등을 구하기)
sequences = char_dataset.batch(config['seq_length']+1 , drop_remainder = True)
dataset = sequences.map(generate_mod.split_input_target)

# 읽어온 텍스트 길이로 버퍼 크기 선정
Buffer_size = len(text_as_int) * 2

# BUFFER_SIZE개로 이루어진 버퍼로 임의의 샘플을 뽑은 후 BATCH_SIZE로 분할한다.
dataset = dataset.shuffle(Buffer_size).batch(config['batch_size'], drop_remainder= True)

# 모델생성
model = generate_mod.model_learning(
    config = config,
    vocab = vocab,
    dataset= dataset,
    genre_Index = 1
    )

#%%
# 생성한 모듈 경로
import generate_mod
# 그 외의 모듈들
import tensorflow as tf

generate_mod.generate_text(
    model_index = 1, 
    start_string = '사건이 ',
    num_generate = 1000,
    temperature = 0.7
    )