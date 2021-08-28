"""
https://developers.kakao.com/ 에서 api키 및 Token을 승인받아 진행

"""

#%%
import requests
import json
with open('../data/kakao_api.json') as fp:
    ka = json.load(fp)
ka
#%%
# 본인이 가지고 있는 Api키 및 토큰을 가지고
# 실제로 사용할 토큰 가져오기
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = ka.rest_api
redirect_uri = 'https://example.com/oauth'
authorize_code = ka.token

# Json 파일로 만들기 위해 shape맞춰줌
data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }
# json형식으로 만들어주기
response = requests.post(url, data=data)
tokens = response.json()

# 저장하기
with open(r"../data/kakao_token.json","w") as fp:
    json.dump(tokens, fp)

    
#%%
import requests
import json

#1.
with open("../data/kakao_token.json","r") as fp:
    tokens = json.load(fp)

#2.
with open("../data/kakao_token.json","r") as fp:
    tokens = json.load(fp)

# 보낼 URL, 카카오 본인에게 보내기는 아래 주소와 같음
url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 헤더
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

#  전송할 데이터
data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"설정지역 : 아프가니스탄\n위험도 : 상\n전쟁날 것 같습니다.\n https://www.google.com/",
        "link":{
            "web_url":"www.naver.com",
            "mobile_web_url":'www.naver.com'
            
        }   
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code

