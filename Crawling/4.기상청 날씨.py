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
                        port=3306,
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

# 추가할 전제 행을 넣을 리스트 
rows = [] 

for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR , 'td')
    
    # td태그의 text가 공백이면 null 처리후 list객체로 반환
    str = list(
                map(lambda td: 'null'                     # 참 = null
                                if td.text.isspace()      # td.text가 공백이면
                                else "'%s'" % (td.text)   # 거짓 = 'td.text' 
                                , tds)                     # 배열 객체
    )

    #  SQL문에 추가할 value로 작성 (col1, col2, co13, ....col14, NOW())
    row = "(%s, NOW())" % (",".join(str))

    # 행 추가
    rows.append(row)

# SQL 실행
cur.execute("INSERT INTO `weather` VALUES " + ",".join(rows))
conn.commit()

# 가상 브라우저 종료
browser.close()

# 데이터베이스 종료
cur.close()
print('insert 완료...')