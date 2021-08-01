#%%
"""
목적 : 공백 및 특수문자제거
"""
import os
import re
# dir_path = '../Scrapping/novels/로맨스/'
dir_path = '../data/harryPoter/'
novel_list = os.listdir(dir_path)
text = ""
for novel in novel_list:
  text += open(dir_path+novel ,'rb').read().decode(encoding='ansi')
def clean(text):
    result = re.sub(' +', ' ', text)    
    result = re.sub('(\r\n)+', '\n', result)
    result = re.sub('\n ', '', result)
    result = re.sub('\n', '\n ', result)
    result = re.sub('\.+','.',result) 
    result = re.sub(r'[_\-·=+,#:/q:^$@;*\"※~&%ㆍ「」『』\\`~"‘|\(\)\[\]\<\>`\'…《》]', '', result)
    result = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]+', '', result)
    return result
file = open('harryPoter.txt', 'w',encoding='utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write(clean(text))      # 파일에 문자열 저장
file.close()      
#%% 
file = open('romance.txt', 'w',encoding='utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write(text)      # 파일에 문자열 저장
file.close()      

#%%
import os
import re
def clean(text):
    # 공백 및 특수문자 제거
    result = re.sub(' +', ' ', text)    
    result = re.sub('(\r\n)+', '\n', result)
    result = re.sub('\n ', '', result)
    result = re.sub('\n', '\n ', result)    
    result = re.sub('\.+','.',result)
    result = re.sub(r'[_\-·=+,#:/q:^$@;*\"※~&%ㆍ「」『』\\`~"‘|\(\)\[\]\<\>`\'…《》]', '', result)
    result = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]+', '', result)

    return result
file_path = '../data/'
file_name = 'toto.txt'
text = open(file_path+file_name,'rb').read().decode(encoding='ansi')
text =clean(text)
file = open(file_name, 'w',encoding='utf-8')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write(text)      # 파일에 문자열 저장
file.close()     
# %%
text

# %%
