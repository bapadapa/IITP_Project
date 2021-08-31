#%%
import re
import urllib.request
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from keras.layers import Embedding, Dense, LSTM,Dropout,GRU,Concatenate
from keras.models import Sequential,Input,Model
from keras.utils import np_utils
from keras.callbacks import EarlyStopping
from keras import optimizers,losses
from sklearn.model_selection import train_test_split
import tensorflow as tf
import json
from bs4 import BeautifulSoup

# %%
path  = '../../data/'
danger = pd.read_csv(path+'newsData/google_news_data_danger_words.csv')
danger =danger[danger.columns[1:]]
safe = pd.read_csv(path+'newsData/google_news_data_safe_words.csv')
safe =safe[safe.columns[1:]]
# %%
print('danger : ',danger.search_word.unique(),'\n',len(danger.search_word.unique()))
print('safe : ' ,safe.search_word.unique() ,'\n', len(safe.search_word.unique()))
# %%
# 위험, 안전 키워드 통일화
new_danger = danger[danger.columns[:-1]]
new_danger.search_word = 0
new_safe = safe[safe.columns[:-1]]
new_safe.search_word = 1

#%%
# 칼럼명 변경
data = new_danger.append(new_safe)
data.columns = ['Text','safety'] 
data.safety = np_utils.to_categorical(data.safety)
pre_clean = len(data)
#%%
# 데이터 정제
# 중복제거
data.drop_duplicates(subset='Text',inplace= True)
# na제 거
data.replace('',np.nan, inplace= True)
data.dropna(how='any')
# Text 정제
#축약 사전
with open(path+'shortCut.json') as fp:
    contraction_mapping = json.load(fp)
stop_words = set(stopwords.words('english'))
def text_cleaner(text,num = 0):
    newString = text.lower()
    newString = BeautifulSoup(newString, "lxml").text
    newString = re.sub(r'\([^)]*\)', '', newString)
    newString = re.sub('"','', newString)
    newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])    
    newString = re.sub(r"'s\b","",newString)
    newString = re.sub("[^a-zA-Z]", " ", newString) 
    newString = re.sub('[m]{2,}', 'mm', newString)
    if(num==0):
        tokens = [w for w in newString.split() if not w in stop_words]
    else:
        tokens=newString.split()
    long_words=[]
    for i in tokens:
        if len(i)>1:                                                 #removing short word
            long_words.append(i)   
    return (" ".join(long_words)).strip()

#call the function`
cleaned_text = []
for t in data['Text']:
    cleaned_text.append(text_cleaner(t))
data['Text'] = cleaned_text
print(len(data))
post_clean = len(data)
print(f'{pre_clean-post_clean}개의 단어가 제거 되었습니다.')

# %%
x = []
for sentence in data['Text']:    
    x.append([word[0] for word in nltk.pos_tag(nltk.word_tokenize(sentence))])
x
#%%
# Tokenizing 해주기
tokenizer = Tokenizer()
# 문자 데이터 -> 리스트 형태로 변경
tokenizer.fit_on_texts(x)
# tokenizer을 key : value, 즉 dict로 만들어줌
print(tokenizer.word_index)
#%%
# 빈도수가 너무 적은 단어는 제거해주기
threshold = 3
words_cnt = len(tokenizer.word_index)
rare_cnt = 0
words_freq = 0
rare_freq = 0

for key, value in tokenizer.word_counts.items():
    words_freq += value
    # 길이가 작으면 rare하다
    if value < threshold:
        rare_cnt +=1
        rare_freq += value
print('전체 단어수 : ', words_cnt)    
print(f"빈도수가 {threshold-1} 이 하인 희귀 단어 수 {rare_cnt}")
print(f'희귀 단어 비율 : {(rare_cnt/words_cnt) * 100}')
print(f"희귀 단어 등장 빈도 비율 : {(rare_freq/words_freq) * 100}")
#%%
vocab_size = words_cnt - rare_cnt +2
print(vocab_size)
#%%
# oov == out of vocabulary
tokenizer = Tokenizer(vocab_size , oov_token = 'OOV')
tokenizer.fit_on_texts(x)
# sentence를 index값 즉 시퀀스로 만들어줌
x = tokenizer.texts_to_sequences(x)
y =np.array(data['safety'])

#%%
# 전처리하면서 길이가 0이된 문장 삭제
drop_ = [idx for idx, sentence in enumerate(x) if len(sentence) < 1]
x = np.delete(x , drop_ ,axis=0)
y = np.delete(y , drop_ ,axis=0)
#%%
#padding 길이를 맞추고, 입력을 동일한 길이로 맞춰줌
print('최대 길이 :  ', max(len(x) for l in x))
print('평균 길이 :  ', sum(map(len, x))/len(x))
#%%
# 플롯팅하여 최대길이 지정해주기
plt.hist([len(s) for s in  x],bins = 50)
plt.xlabel('length')
plt.ylabel('number')
plt.show()
#%%
max_len = 15
x= pad_sequences(x,maxlen=max_len)
#%%
X_train, X_test, Y_train,Y_test = train_test_split(x,y,test_size=.2)
# %%
# Sequential로 생성
# 이전 Layer의 Tensor list를 다음 Layer로 전달.
model = Sequential([
    Embedding(vocab_size, 256),
    LSTM(512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.5,recurrent_dropout=0.5),    
    LSTM(512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.5,recurrent_dropout=0.5),    
    LSTM(512,kernel_initializer='he_uniform',dropout=.5,recurrent_dropout=0.5),    
    Dense(256, activation='relu',kernel_initializer='he_uniform'),
    Dropout(.5),
    Dense(128, activation='relu',kernel_initializer='he_uniform'),
    Dropout(.5),
    Dense(128, activation='relu',kernel_initializer='he_uniform'),
    Dense(1, activation='sigmoid')
])
model.summary()
model.compile(
    loss = losses.BinaryCrossentropy(),
    optimizer= optimizers.RMSprop(learning_rate=1e-5),    
    metrics = ['accuracy']
)
#%%
# Concatenate 을 이용하여 분할처리
# 연결 축을 제외하고는 모두 동일한 모양 인 Tensor List을 입력으로 취하고 모든 입력을 연결 한 Unit Tensor를 반환합니다.
input_a = Input(shape=X_train.shape[1:])
embedding_layer = Embedding(vocab_size,256)(input_a)
# gru_layer = GRU(512,kernel_initializer='he_uniform',dropout=.4,recurrent_dropout=0.4)(embedding_layer)
lstm_layer01 = LSTM(512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.4,recurrent_dropout=0.4)(embedding_layer)
lstm_layer02 = LSTM(512,kernel_initializer='he_uniform' ,return_sequences=True,dropout=.4,recurrent_dropout=0.4)(embedding_layer)
# merge_layer = Concatenate()([gru_layer , lstm_layer])
merge_layer = Concatenate()([lstm_layer01 , lstm_layer02])
fc_layer01 = Dense(512, activation='relu',kernel_initializer='he_uniform')(merge_layer)
fc_layer01 = Dropout(.4)(fc_layer01)

fc_layer02 = Dense(512, activation='relu',kernel_initializer='he_uniform')(fc_layer01)
fc_layer02 = Dropout(.4)(fc_layer02)
# fc_layer = Dense(256, activation='relu',kernel_initializer='he_uniform')(fc_layer)
output_a = Dense(1,activation='sigmoid')(fc_layer02)
# output_a = Dense(1,activation='sigmoid')(fc_layer)

model = Model(inputs= [input_a],outputs = [output_a])
model.summary() 
model.compile(
    loss = losses.BinaryCrossentropy(),
    optimizer = optimizers.RMSprop(learning_rate= 1e-5),
    metrics = ['accuracy']
)
#%%
model.summary()
#%%
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1,patience=50)
# model = keras.models.load_model(path+'models/Concatenate_LSTM3_dropout5_RMSPropmodel.h5')

with tf.device('/device:GPU:0'):
    history = model.fit(
        x = X_train,
        y = Y_train,
        callbacks=[es],
        epochs= 1000,
        batch_size= 512,
        validation_split= .3
    )
model.save(path+'models/Concatenate_LSTM3_dropout5_RMSProp_model.h5')
#%%
path
#%%
#훈련결과 확인
hist_dict = history.history
loss = hist_dict['loss']
val_loss = hist_dict['val_loss']
acc = hist_dict['accuracy']
val_acc = hist_dict['val_accuracy']

plt.plot(loss, 'b--', label = 'train loss')
plt.plot(val_loss, 'r:' , label = 'val loss')
plt.legend()
plt.grid()

plt.figure()
plt.plot(acc, 'b--', label = 'train acc')
plt.plot(val_acc, 'r:' , label = 'val acc')
plt.legend()
plt.grid()

plt.show()
#%%
results = model.evaluate(X_test, Y_test)


#%%
results

#%%
class_names = [
    'danger', 'Safe'
    ]
print(class_names[np.argmax(model.predict(X_test[200:201]))])
print(class_names[np.argmax(Y_test[200:201])])
