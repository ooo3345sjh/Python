"""
날짜 : 2023/03/06
이름 : 서정현
내용 : LeMo DB 업로드
"""
import pymysql
import time
import uuid
import os
from openpyxl import Workbook, load_workbook
from random import randrange
import win32com.client

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='lemo', 
                        port=3306,
                        charset='utf8')

# SQL 실행객체
cur = conn.cursor()

# 1. 불러올 파일의 위치 지정
filename = 'C:/Users/java2/Desktop/lemoDB.xlsx'

# 2. openpyxl을 통해서 엑셀파일을 열기
wb = load_workbook(filename, data_only=True)

# 3. 불러온 Workbook의 sheet확인
accommodation = wb['숙소']

rows = accommodation['A2':'A4584']

rowsList = []

for row in rows:
    rowList = []
    for cell in  row:
        rowList.append(str(cell.value).replace("'", ""))
    rowsList.append(rowList)

# lemo_product_accommodation(숙소) INSERT SQL문
acc_sql = "INSERT INTO `lemo_product_ratepolicy` (`acc_id`, `rp_offSeason_weekday`, `rp_offSeason_weekend`, `rp_peakSeason_weekday`, `rp_peakSeason_weekend`) VALUES"

accList = []
for index, row in enumerate(rowsList):
    acc_id = row[0]
    rp_offSeason_weekday = str(5)
    rp_offSeason_weekend = str(5)
    rp_peakSeason_weekday = str(5)
    rp_peakSeason_weekend = str(5)

    accList_vlaues = []
    accList_vlaues.insert(0, "'" + acc_id + "'")
    accList_vlaues.insert(1, "'" + rp_offSeason_weekday + "'")
    accList_vlaues.insert(2, "'" + rp_offSeason_weekend + "'")
    accList_vlaues.insert(3, "'" + rp_peakSeason_weekday + "'")
    accList_vlaues.insert(4, "'" + rp_peakSeason_weekend + "'")

    accList.append('({})'.format(','.join(accList_vlaues)))

acc_sql = acc_sql + ','.join(accList)


# SQL 실행
cur.execute(acc_sql)
conn.commit()

# 데이터베이스 종료
cur.close()