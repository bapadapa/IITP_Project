"""
Text Summarization

"""

#%%
import numpy as np
from numpy.core.fromnumeric import shape
from numpy.core.numeric import NaN 
import pandas as pd
import re

from bs4 import BeautifulSoup
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import  LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional
from keras.preprocessing.text import Tokenizer 
from keras.preprocessing.sequence import pad_sequences
from keras.models import Model, Input
from keras.callbacks import EarlyStopping
from keras import backend as K 

import urllib
urllib.request.urlretrieve("https://raw.githubusercontent.com/thushv89/attention_keras/master/src/layers/attention.py", filename="attention.py")
from attention import AttentionLayer

from scipy.sparse.construct import random

from sklearn.model_selection import train_test_split

import tensorflow as tf

from nltk.corpus import stopwords

import matplotlib.pyplot as plt


import warnings
from tensorflow.python import keras

from tensorflow.python.keras import activations
import json
# Warning 제거 및 칼럼 여러개 보기
warnings.filterwarnings("ignore")
pd.set_option("display.max_colwidth", 200)

data=pd.read_csv(r'..\..\data\sample_data\Reviews.csv',nrows=10000)

with open('../../data/shortCut.json') as fp:
    contraction_mapping = json.load(fp)
    
data.drop_duplicates(subset=['Text'],inplace=True)#dropping duplicates
data.dropna(axis=0,inplace=True)#dropping na

stop_words = set(stopwords.words('english')) 


def to_token(train,val,max_len,thresh =4):
    #prepare a tokenizer for reviews on training data
    tokenizer_ = Tokenizer() 
    tokenizer_.fit_on_texts(list(train))

    cnt=0
    tot_cnt=0
    freq=0
    tot_freq=0

    for key,value in tokenizer_.word_counts.items():
        tot_cnt=tot_cnt+1
        tot_freq=tot_freq+value
        if(value<thresh):
            cnt=cnt+1
            freq=freq+value

    # print("% of rare words in vocabulary:",(cnt/tot_cnt)*100)
    # print("Total Coverage of rare words:",(freq/tot_freq)*100)


    #prepare a tokenizer for reviews on training data
    tokenizer_ = Tokenizer(num_words=tot_cnt-cnt) 
    tokenizer_.fit_on_texts(list(train))

    #convert text sequences into integer sequences
    train_seq    =   tokenizer_.texts_to_sequences(train) 
    val_seq   =   tokenizer_.texts_to_sequences(val)

    #padding zero upto maximum length
    train    =   pad_sequences(train_seq,  maxlen=max_len, padding='post')
    val   =   pad_sequences(val_seq, maxlen=max_len, padding='post')

    #size of vocabulary ( +1 for padding token)
    voc   =  tokenizer_.num_words + 1
    return tokenizer_,train,val,voc

def text_cleaner(text,num):
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

#call the function
cleaned_text = []
for t in data['Text']:
    cleaned_text.append(text_cleaner(t,0)) 

#call the function
cleaned_summary = []
for t in data['Summary']:
    cleaned_summary.append(text_cleaner(t,1))
data['cleaned_text']=cleaned_text
data['cleaned_summary']=cleaned_summary
data.replace('', np.nan, inplace=True)
data.dropna(axis=0,inplace=True)

text_word_count = []
summary_word_count = []

max_text_len=30
max_summary_len=15

cleaned_text =np.array(data['cleaned_text'])
cleaned_summary=np.array(data['cleaned_summary'])

short_text=[]
short_summary=[]

for i in range(len(cleaned_text)):
    if(len(cleaned_summary[i].split())<=max_summary_len and len(cleaned_text[i].split())<=max_text_len):
        short_text.append(cleaned_text[i])
        short_summary.append(cleaned_summary[i])
        
df=pd.DataFrame({'text':short_text,'summary':short_summary})

df['summary'] = df['summary'].apply(lambda x : 'start '+ x + ' end')

x_train,x_val,y_train,y_val=train_test_split(np.array(df['text']),np.array(df['summary']),test_size=0.1,random_state=0,shuffle=True) 

x_tokenizer,x_train,x_val,x_voc = to_token(x_train,x_val,max_text_len , thresh= 4)
y_tokenizer,y_train,y_val,y_voc = to_token(y_train,y_val,max_summary_len , thresh= 6)

ind=[]
for i in range(len(y_train)):
    cnt=0
    for j in y_train[i]:
        if j != 0 :
            cnt += 1 
    if(cnt==2):
        ind.append(i)

y_train=np.delete(y_train,ind, axis=0)
x_train=np.delete(x_train,ind, axis=0)

ind=[]

for i in range(len(y_val)):
    cnt=0
    for j in y_val[i]:
        if j!=0:
            cnt=cnt+1
    if(cnt==2):
        ind.append(i)

y_val=np.delete(y_val,ind, axis=0)
x_val=np.delete(x_val,ind, axis=0)

# -----------------------------------------------------------------------------
K.clear_session()

latent_dim = 512
embedding_dim=128

# Encoder
enc_inputs = Input(shape=(max_text_len,))

#embedding layer
enc_emb =  Embedding(x_voc, embedding_dim,trainable=True)(enc_inputs)

#encoder lstm 1
enc_output1, state_h1, state_c1 = LSTM(latent_dim,return_sequences=True,return_state=True,dropout=0.4,recurrent_dropout=0.4)(enc_emb)

#encoder lstm 2
enc_output2, state_h2, state_c2 = LSTM(latent_dim,return_sequences=True,return_state=True,dropout=0.4,recurrent_dropout=0.4)(enc_output1)

#encoder lstm 3
enc_outputs, state_h, state_c=LSTM(latent_dim, return_state=True, return_sequences=True,dropout=0.4,recurrent_dropout=0.4)(enc_output2)


# Set up the decoder, using `encoder_states` as initial state.
dec_inputs = Input(shape=(None,))

#embedding layer
dec_emb_layer = Embedding(y_voc, embedding_dim,trainable=True)
dec_emb = dec_emb_layer(dec_inputs)

dec_lstm = LSTM(latent_dim, return_sequences=True, return_state=True,dropout=0.4,recurrent_dropout=0.2)
dec_outputs,decoder_fwd_state, decoder_back_state = dec_lstm(dec_emb,initial_state=[state_h, state_c])

# Attention layer
attn_layer = AttentionLayer(name='attention_layer')
attn_out, attn_states = attn_layer([enc_outputs, dec_outputs])

# Concat attention input and decoder LSTM output
dec_con_input = Concatenate(axis=-1, name='concat_layer')([dec_outputs, attn_out])

#dense layer
dec_dense =  TimeDistributed(Dense(y_voc, activation='softmax'))
dec_outputs = dec_dense(dec_con_input)

# Define the model 
model = Model([enc_inputs, dec_inputs], dec_outputs)

model.summary() 

model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1,patience=10)

with tf.device("/device:gpu:0"):
    history=model.fit(
        [x_train,y_train[:,:-1]], 
        y_train.reshape(y_train.shape[0],y_train.shape[1], 1)[:,1:] ,
        epochs=50,
        callbacks=[es],
        batch_size=256,
        validation_data=(
            [x_val,y_val[:,:-1]],
            y_val.reshape(y_val.shape[0],y_val.shape[1], 1)[:,1:]
            )
        )


plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
plt.show()

r_target_word_idx=y_tokenizer.index_word
r_source_word_idx=x_tokenizer.index_word
target_word_idx=y_tokenizer.word_index

# Encode the input sequence to get the feature vector
enc_model = Model(inputs=enc_inputs,outputs=[enc_outputs, state_h, state_c])

# Decoder setup
# Below tensors will hold the states of the previous time step
dec_state_input_h = Input(shape=(latent_dim,))
dec_state_input_c = Input(shape=(latent_dim,))
dec_hidden_state_input = Input(shape=(max_text_len,latent_dim))

# Get the embeddings of the decoder sequence
dec_emb2= dec_emb_layer(dec_inputs) 
# To predict the next word in the sequence, set the initial states to the states from the previous time step
dec_outputs2, state_h2, state_c2 = dec_lstm(dec_emb2, initial_state=[dec_state_input_h, dec_state_input_c])

#attention inference
attn_out_inf, attn_states_inf = attn_layer([dec_hidden_state_input, dec_outputs2])
dec_inf_concat = Concatenate(axis=-1, name='concat')([dec_outputs2, attn_out_inf])

# A dense softmax layer to generate prob dist. over the target vocabulary
dec_outputs2 = dec_dense(dec_inf_concat) 

# Final decoder model
dec_model = Model(
    [dec_inputs] + [dec_hidden_state_input,dec_state_input_h, dec_state_input_c],
    [dec_outputs2] + [state_h2, state_c2]) 
def dec_sequence(input_seq,target_word_idx,r_target_word_idx,max_summary_len):
    # Encode the input as state vectors.
    e_out, e_h, e_c = enc_model.predict(input_seq)
    
    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1,1))
    
    # Populate the first word of target sequence with the start word.
    target_seq[0, 0] = target_word_idx['start']

    stop_condition = False
    dec_sentence = ''
    while not stop_condition:
      
        output_tokens, h, c = dec_model.predict([target_seq] + [e_out, e_h, e_c])

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = r_target_word_idx[sampled_token_index]
        
        if(sampled_token!='end'):
            dec_sentence += ' '+sampled_token

        # Exit condition: either hit max length or find stop word.
        if (sampled_token == 'end'  or len(dec_sentence.split()) >= (max_summary_len-1)):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1,1))
        target_seq[0, 0] = sampled_token_index

        # Update internal states
        e_h, e_c = h, c

    return dec_sentence

def seq2summary(input_seq,target_word_idx,r_target_word_idx):
    newString=''
    for i in input_seq:
        if((i!=0 and i!=target_word_idx['start']) and i!=target_word_idx['end']):
            newString=newString+r_target_word_idx[i]+' '
    return newString

def seq2text(input_seq,r_source_word_idx):
    newString=''
    for i in input_seq:
        if(i!=0):
            newString=newString+r_source_word_idx[i]+' '
    return newString


for i in range(0,100):
    print("Review:",seq2text(x_train[i],r_source_word_idx))
    print("Original summary:",seq2summary(y_train[i],target_word_idx,r_target_word_idx))
    print("Predicted summary:",dec_sequence(x_train[i].reshape(1,max_text_len),target_word_idx,r_target_word_idx,max_summary_len))
    print("\n")
#%%
