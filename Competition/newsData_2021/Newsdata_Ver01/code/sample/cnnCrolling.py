"""
CNN 크롤링
"""

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import json

from time import sleep
import os
from bs4 import BeautifulSoup
import pandas as pd
import json

# Json 읽기
with open("../../data/Crawling.json", 'r', encoding = 'utf-8') as common:
        config = json.load(common)
# save_path = os.path.join(os.getcwd(),"New_NCBI_metadata")
# Path 에 디렉토리가 없으면 생성해줌
# if not os.path.isdir(save_path):
#         os.mkdir(save_path)

# 크롬브라우저를 백그라운드로 실행하게 해줌
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# options.add_experimental_option("prefs", {
#     ## "excludeSwitches":["enable-logging"],
#     "download.default_directory": save_path
# })

browser = webdriver.Chrome(executable_path=config['driver_path'],chrome_options=options)
# 최종적으로 다운로드 여부 확인하기위해 생성
wait = WebDriverWait(browser, 30)

target = 'Afghanistan'
print("Start Crawling! \n")

browser.get(config['cnn_path']+target)

# 기사 개수 가져오기
soup = BeautifulSoup(browser.page_source,'html.parser')
a = soup.find('div',{'class':'cnn-search__results-count'}).text
total_page = (int(a.split()[-3])//50+1)
# for page in range(total_page):

# 가져온 기사 개수 기반으로 검색
url_list = []
title_list = []
for page in range(total_page):
    if page % 20 == 19:
        browser.close()
        # browser = webdriver.Chrome(executable_path=config['driver_path'],chrome_options=options)
        browser = webdriver.Chrome(executable_path=config['driver_path'])
        print('browser reset')
        sleep(1)
    print(f"current={page+1} page={total_page}")     
    browser.get(config['cnn_path']+target+f"&from={page*50}&page={page+1}")    
    try:
        wait.until(EC.presence_of_element_located(((By.CLASS_NAME,'cnn-search__result-headline'))))
        sleep(2)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        lists = soup.find("div",{"class":"cnn-search__results-list"})
        list = lists.findAll("h3",{"class":"cnn-search__result-headline"})        
        url_list += [div.find("a")['href'] for div in list]
        title_list += [div.find("a").text for div in list]
        print(len(url_list),len(title_list))
        print(title_list[page*50])
    except:
        print('scrapted error')
        pass

df = pd.DataFrame({'title':title_list,'link' : url_list},columns={'title':'link'})
df.to_csv('../../data/Afghanistan.csv',encoding = 'utf-8-sig')
#%%
lists = soup.find("div",{"class":"cnn-search__results-list"})
list = lists.findAll("h3",{"class":"cnn-search__result-headline"})
url_list = [div.find("a")['href'] for div in list]
title_list =  [div.find("a").text for div in list]
browser.find_element_by_class_name('icon icon--arrow-right').click()            
# browser.close()
#%%

# %%
browser.get(url_list[2])

title_list[1]
#%%
a = soup.findAll('div',{'class':'l-container'})
for i in a:
    print(i.text)
# %%

