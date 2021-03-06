"""
문피아 크롤링

미니 프로젝트 ( Text Genration ) 를 위한 소설 크롤링/스크랩핑
"""
#%%
# -------------------------------------------------------
# !pip install selenium
# !pip install bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from time import sleep
import os

import pandas as pd
import json
import re
# Json 파일 읽기
with open("config.json", "r", encoding = 'utf-8') as common:
    config = json.load(common)
webPath = config['webPath']
filePath = config['novel_Path']

# 다운로드 경로
if not os.path.isdir(filePath):
    os.mkdir(filePath)

# 크롬경로 등 기본 설정
prefs = {config['chromeDownload']: filePath}
chrome_option = Options()
chrome_option.add_experimental_option('prefs',prefs)

# 웹 드라이버 생성
# 위에 설정한 기본 옵션 삽입.
driver = webdriver.Chrome(config['chromePath'],options=chrome_option)
driver.implicitly_wait(3)
title_link = pd.DataFrame(columns=['genre','title','link'])

# 크롤링 시작    
for genre in config['genres'] :
    driver.get(webPath)
    sleep(2)
    # 장르 목록창 클릭
    driver.find_element_by_class_name("trigger-genres").click()
    sleep(2)
    # 장르 선택
    menus = driver.find_element_by_id("NAV-GENRES")
    menus.find_element_by_link_text(genre[0]).click()
    sleep(2)

    # 완결작 클릭
    driver.find_element_by_class_name("pic-sect-close").click()
    sleep(2)    
    soup = BeautifulSoup(driver.page_source,'html.parser')
    lists = soup.find("ul",{"class":"unstyled mu row"})
    lis = lists.findAll("a",{"class":"title"})
    # url 리스트 가져오기    
    for at in lis:
        title_link= title_link.append({'genre':genre[0],'title' : at['title'] ,'link':at['href']} ,ignore_index=True)

    for i in range(len(title_link)):
        driver.get(title_link.link[i]) 
        novel = str()
        try:
            sleep(1)
            driver.find_element_by_class_name('first-view').click()
        except:
            pass
        
        while True:    
            try:    
                # WebDriverWait(driver,15).until(
                #     EC.presence_of_element_located(By.CLASS_NAME,"tcontent"))               
                sleep(1)
                novel += driver.find_element_by_class_name('tcontent').text
                driver.find_element_by_class_name('next').click() 
            except:
                break    
        if not os.path.isdir(filePath+'/'+genre[1]):
            os.mkdir(filePath+'/'+genre[1])
        fileName = re.sub('[^a-zA-Z0-9가-힣\.\?\!\s]', '', title_link.title[i])
        with open(f"{filePath}/{genre[1]}/{fileName}.txt", "w" , encoding = 'utf-8-sig') as file:
            file.write(novel)
            file.close()
driver.close()
# %%
import json
import re
# Json 파일 읽기
with open("config.json", "r", encoding = 'utf-8') as common:
    config = json.load(common)
for genre in config['genres'] :
    print(genre[1])