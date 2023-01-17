"""
날짜 : 2023/01/17
이름 : 서정현
내용 : 파이썬 기상청 날씨 크롤링 실습하기
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='java2db', 
                        charset='utf8')

# SQL 실행객체
cur = conn.cursor()





# 가상 브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

# 페이지 이동
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 지역명 출력
trs = browser.find_elements(By.CSS_SELECTOR, "#weather_table > tbody > tr")

# SQL 실행
sql = "INSERT INTO `weather` VALUES "


list = []
for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR , 'td')

    str = "("
    for i in range(13):
        if i == 12: 
            str += "\'" + tds[i].text + "\', NOW())"
            break

        str += 'null' if tds[i].text == " " else "\'" + tds[i].text + "\'"
        str += ','
    list.append(str)



result = ",".join(list)


sql += result
print(sql)
cur.execute(sql)
conn.commit()

# 가상 브라우저 종료
browser.close()

# 데이터베이스 종료
cur.close()
print('insert 완료...')
