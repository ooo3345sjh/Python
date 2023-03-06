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

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='lemo', 
                        charset='utf8')

# SQL 실행객체
cur = conn.cursor()

# 1. 불러올 파일의 위치 지정
filename = 'C:/Users/java2/Desktop/lemoDB.xlsx'

# 2. openpyxl을 통해서 엑셀파일을 열기
wb = load_workbook(filename, data_only=True)

# 3. 불러온 Workbook의 sheet확인
sellerList = wb['판매자']

rows = sellerList['A2':'L344']

rowsList = []

for row in rows:
    rowList = []
    for cell in  row:
        rowList.append(str(cell.value))
    rowsList.append(rowList)



# lemo_member_userId(회원 아이디) INSERT SQL문
userId_sql = "INSERT INTO `lemo_member_userId` (`userId_id`, `userId_nick`, `userId_type`) VALUES"
userIdList = []

# lemo_member_user(회원) INSERT SQL문
user_sql = "INSERT INTO `lemo_member_user` (`userId_id`, `user_pass`, `user_hp`, `user_hp_certi`, `user_role`, `user_regip`, `user_rdate`) VALUES"
userList = []

# lemo_member_businessInfo(비즈니스 정보) INSERT SQL문
businessInfo_sql = "INSERT INTO `lemo_member_businessInfo` (`userId_id`, `bis_company`, `bis_ceo`, `bis_openDate`, `bis_bizRegNum`, `bis_tel`, `bis_zip`, `bis_addr`, `bis_addrDetail`) VALUES"
businessInfoList = []

for index, row in enumerate(rowsList):
    userId_id = str(index) + row[0]
    userId_nick = row[1]
    userId_type = row[2]
    user_hp = str(randrange(1000)) + row[3][:-3]
    user_hp_certi = "1"
    user_role = "BUSINESS"
    user_regip = "0:0:0:0:0:0:0:1"
    user_rdate = "NOW()"
    bis_company = row[4]
    bis_ceo = row[5]
    bis_openDate = row[6]
    bis_bizRegNum = row[7].replace("-", "")[: -4] + str(randrange(10000))
    bis_zip = row[9]
    bis_addr = row[10]
    bis_addrDetail = row[11]


    userId_values = []
    userId_values.insert(0, "'" + userId_id + "'")
    userId_values.insert(1, "'" + userId_nick + "'")
    userId_values.insert(2, "'" + userId_type + "'")
    userIdList.append('({})'.format(','.join(userId_values)))

    user_vlaues = []
    user_vlaues.insert(0, "'" + userId_id + "'")
    user_vlaues.insert(1, "'" + "1234" + "'")
    user_vlaues.insert(2, "'" + user_hp + "'")
    user_vlaues.insert(3, "'" + user_hp_certi + "'")
    user_vlaues.insert(4, "'" + user_role + "'")
    user_vlaues.insert(5, "'" + user_regip + "'")
    user_vlaues.insert(6, user_rdate)
    userList.append('({})'.format(','.join(user_vlaues)))

    businessInfoList_vlaues = []
    businessInfoList_vlaues.insert(0, "'" + userId_id + "'")
    businessInfoList_vlaues.insert(1, "'" + bis_company + "'")
    businessInfoList_vlaues.insert(2, "'" + bis_ceo + "'")
    businessInfoList_vlaues.insert(3, "'" + bis_openDate + "'")
    businessInfoList_vlaues.insert(4, "'" + bis_bizRegNum + "'")
    businessInfoList_vlaues.insert(5, "'" + user_hp + "'")
    businessInfoList_vlaues.insert(6, "'" + bis_zip + "'")
    businessInfoList_vlaues.insert(7, "'" + bis_addr + "'")
    businessInfoList_vlaues.insert(8, "'" + bis_addrDetail + "'")
    businessInfoList.append('({})'.format(','.join(businessInfoList_vlaues)))
    
userId_sql = userId_sql + ','.join(userIdList)
user_sql = user_sql + ','.join(userList)
businessInfo_sql = businessInfo_sql + ','.join(businessInfoList)

# SQL 실행
cur.execute(userId_sql)
conn.commit()
cur.execute(user_sql)
conn.commit()
cur.execute(businessInfo_sql)
conn.commit()

# 데이터베이스 종료
cur.close()