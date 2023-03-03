"""
날짜 : 2023/03/03
이름 : 서정현
내용 : 여기어때 데이터 크롤링
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

# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 여기어때 검색 페이지 이동
browser.get('https://www.goodchoice.kr/product/result?keyword=%EB%B6%80%EC%82%B0')

# 검색된 숙소 리스트
lists = browser.find_elements(By.CSS_SELECTOR, "#poduct_list_area > ul > li")

# 상세보기 페이지 링크를 저장할 배열 선언
links = []

# 배열에 링크 주소 값 저장
for list in lists:
    a = list.find_element(By.CSS_SELECTOR , 'a')
    links.append(a.get_attribute('href'))

# 검색 페이지 닫기
browser.close

# 각 숙소 리스트 상세 페이지 브라우저 열기
for link in links:
    browser.get(link)
    time.sleep(5)
    browser.close


    

# 가상 브라우저 종료
#browser.close()
