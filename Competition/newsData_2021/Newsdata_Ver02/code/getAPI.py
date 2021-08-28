#%%
import json
import requests

with open("../data/api.json","r") as fp:
    api_key = json.load(fp)
api_key

#%%
datas = {
    "access_key": api_key['access_key'],
    "argument": {
        "query": "서비스 AND 출시",
        "published_at": {
            "from": "2019-01-01",
            "until": "2019-03-31"
        },
        "provider": [
            "경향신문",
        ],
        "category": [
            "정치>정치일반",
            "IT_과학"
        ],
        "category_incident": [
            "범죄",
            "교통사고",
            "재해>자연재해"
        ],
        "byline": "",
        "provider_subject": [
            "경제", '부동산'
        ],
        "subject_info": [
            ""
        ],
        "subject_info1": [
            ""
        ],
        "subject_info2": [
            ""
        ],
        "subject_info3": [
            ""
        ],
        "subject_info4": [
            ""
        ],
        "sort": {"date": "desc"},
        "hilight": 200,
        "return_from": 0,
        "return_size": 5,
        "fields": [
            "content",
            "byline",
            "category",
            "category_incident",
            "provider_news_id",
            "url"
        ]
    }
}
headers = {'Content-Type': 'application/json; chearset=utf-8'}

response = requests.post(api_key['base_url'], headers=headers,data = json.dumps(datas))

response.json()



#%%

datas = {
    "access_key": api_key['access_key'],
    "argument": {
        "news_ids": [
            "01500701.2015083110018412570",
            "01100701.20150826100000152"
        ],
        "fields": [
            "content",
            "byline",
            "category",
            "category_incident",
            "images",
            "provider_subject",
            "provider_news_id",
            "publisher_code"
        ]
    }
}

headers = {'Content-Type': 'application/json; chearset=utf-8'}

response = requests.post(api_key['base_url'], headers=headers,data = json.dumps(datas))
response.json()
#%%
response.text