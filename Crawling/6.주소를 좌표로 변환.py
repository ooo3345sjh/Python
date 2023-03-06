"""
날짜 : 2023/03/03
이름 : 서정현
내용 : 주소를 좌표로 변환
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql
import time

####### 도로명주소 위도 경도 값으로 바꿔주기 ########
# from geopy.geocoders import Nominatim
# geo_local = Nominatim(user_agent='South Korea')

# # 위도, 경도 반환하는 함수
# def geocoding(address):
#     try:
#         geo = geo_local.geocode(address)
#         x_y = [geo.latitude, geo.longitude]
#         return x_y

#     except:
#         return [0,0]


address = "진남로384번길 18"
# geo = geocoding(address)
# print(geo)


import requests, json

# 카카오맵 API 요청 및 지오코딩 함수 임포트
def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    # 'KaKaoAK '는 그대로 두고 개인키만 지우고 입력
    headers = {"Authorization": "KakaoAK 774c9bcb3bb773884b71317afda40365"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    address = api_json['documents'][0]['address']
    crd = {"lat": str(address['y']), "lng": str(address['x'])} 
    address_name = address['address_name']

    return crd



crd = get_location(address)
print(crd)


# 태그 제거 방법
import re

def remove_html(sentence) :
	sentence = re.sub('(<([^>]+)>)', '', sentence)
	return sentence
    
sentence = '나는 지금 <span class="mark">화장품</span>을 <strong>사러</strong> <em>가고</em> 있다.'
sentence = remove_html(sentence)
print(sentence)