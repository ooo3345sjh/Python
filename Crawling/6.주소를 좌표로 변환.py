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
from geopy.geocoders import Nominatim
geo_local = Nominatim(user_agent='South Korea')

# 위도, 경도 반환하는 함수
def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    except:
        return [0,0]


address = "부산 부산진구 진남로384번길 18"
geo = geo_local.geocode(address)
print(geo.longitude, geo.latitude)