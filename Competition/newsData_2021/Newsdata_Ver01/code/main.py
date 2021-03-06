#%%
import googletrans
import re
import urllib.request
import keras
import numpy as np
from numpy.core.numeric import NaN
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
from scipy.sparse.construct import random
from sklearn.model_selection import train_test_split
import tensorflow as tf
import requests
import json
import random
from bs4 import BeautifulSoup
from tensorflow.python.ops.gen_logging_ops import Print
#%%
translate = googletrans.Translator()
path  = '../data/'
with open(path+'shortCut.json') as fp:
    contraction_mapping = json.load(fp)    
country_ = pd.read_csv(path+'newsData/google_news_data_country_words.csv')
country_text = pd.read_csv(path+'newsData/google_news_data_country_words.csv')

model = keras.models.load_model(path+'models/Concatenate_LSTM3_dropout5_RMSProp_model.h5')
danger = pd.read_csv(path+'newsData/google_news_data_danger_words.csv')
danger =danger[danger.columns[1:]]
safe = pd.read_csv(path+'newsData/google_news_data_safe_words.csv')
safe =safe[safe.columns[1:]]

#%%
# ------------------------------------------------------
# functions
def text_cleaner(text,stop_words,num = 0):
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
def dataClean(data):
    # ????????? ??????
    # ????????????
    data.drop_duplicates(subset='Text',inplace= True)
    # na??? ???
    data.replace('',np.nan, inplace= True)
    data.dropna(how='any')
    # Text ??????
    #?????? ??????
    stop_words = set(stopwords.words('english'))

    #call the function`
    cleaned_text = []
    for t in data['Text']:
        cleaned_text.append(text_cleaner(t,stop_words))
    data['Text'] = cleaned_text 
    
    x = []
    for sentence in data['Text']:    
        x.append([word[0] for word in nltk.pos_tag(nltk.word_tokenize(sentence))]) 
    return x     


# ?????? ??? ?????? ????????? ?????????????????? ???????????? ??????
danger = danger[:len(safe)]  
# ??????, ?????? ????????? ?????????
new_danger = danger[danger.columns[:-1]]
new_danger.search_word = 0
new_safe = safe[safe.columns[:-1]]
new_safe.search_word = 1
 
# ????????? ??????
data = new_danger.append(new_safe)
data.columns = ['Text','safety'] 
data.safety = np_utils.to_categorical(data.safety) 

x  = dataClean(data)
# Tokenizing ?????????
tokenizer = Tokenizer()
# ?????? ????????? -> ????????? ????????? ??????
tokenizer.fit_on_texts(x) 
# ???????????? ?????? ?????? ????????? ???????????????
threshold = 3
words_cnt = len(tokenizer.word_index)
rare_cnt = 0
words_freq = 0
rare_freq = 0

for key, value in tokenizer.word_counts.items():
    words_freq += value
    # ????????? ????????? rare??????
    if value < threshold:
        rare_cnt +=1
        rare_freq += value 

vocab_size = words_cnt - rare_cnt +2 

# oov == out of vocabulary
tokenizer = Tokenizer(vocab_size , oov_token = 'OOV')
tokenizer.fit_on_texts(x)  

country_.columns = ['idx','Text','country','url']
country_Name = 'Afghanistan'
target = country_[country_['country'] == country_Name]
target = target.reset_index()
x_country = tokenizer.texts_to_sequences(dataClean(target))  

 
# ?????????????????? ????????? 0?????? ?????? ??????
drop_ = [idx for idx, sentence in enumerate(x_country) if len(sentence) < 1]
x_country = np.delete(x_country , drop_ ,axis=0)
target = np.delete(target , drop_ ,axis=0) 

max_len = 15
x_country= pad_sequences(x_country,maxlen=max_len) 
 
result = model.predict(x_country)

choice_num = random.choice(np.where(result < 0.3)[0])

news_title = country_text.iloc[target.idx[choice_num]].title
news_link = country_text.iloc[target.idx[choice_num]].link
news_title = translate.translate(news_title,src='en',dest='ko').text

# ?????????????????? ??????

with open("../data/kakao/kakao_token.json","r") as fp:
    tokens = json.load(fp) 
# ?????? URL, ????????? ???????????? ???????????? ?????? ????????? ??????
url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# ??????
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

#  ????????? ?????????
data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"???????????? : {}\n ????????? ?????? : {:.2f}%\n{}\n {}".format(country_Name,float(result[choice_num])*100,news_title,news_link),
        "link":{
            "web_url":"www.naver.com"            
        }   
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code 