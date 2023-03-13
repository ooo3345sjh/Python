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
                        port=3307,
                        charset='utf8')

# SQL 실행객체
cur = conn.cursor()

# 1. 불러올 파일의 위치 지정
filename = 'C:/Users/ooo33.DESKTOP-56U45AS/Desktop/lemoDB/lemoDB.xlsx'

# 2. openpyxl을 통해서 엑셀파일을 열기
wb = load_workbook(filename, data_only=True)

# 3. 불러온 Workbook의 sheet확인
sellerList = wb['판매자']

rows = sellerList['A2':'L4557']

rowsList = []

for row in rows:
    rowList = []
    for cell in  row:
        rowList.append(str(cell.value).replace("'", ""))
    rowsList.append(rowList)

# lemo_member_userInfo(회원정보) INSERT SQL문
userInfo_sql = "INSERT INTO `lemo_member_userInfo` (`user_id`, `hp`, `nick`, `type`, `role`, `regip`) VALUES"
userInfoList = []

# lemo_member_user(회원) INSERT SQL문
user_sql = "INSERT INTO `lemo_member_user` (`user_id`, `pass`) VALUES"
userList = []

# lemo_member_businessInfo(비즈니스 정보) INSERT SQL문
businessInfo_sql = "INSERT INTO `lemo_member_businessInfo` (`user_id`, `bis_company`, `bis_ceo`, `bis_openDate`, `bis_bizRegNum`, `bis_tel`, `bis_zip`, `bis_addr`, `bis_addrDetail`) VALUES"
businessInfoList = []


userId_id_list = []
for index, row in enumerate(rowsList):
    user_id = str(index) + row[0] if (index < 343) else row[0]
    nick = row[1]
    type = str(1)
    hp = row[3].replace("-", "")[:8] + str(randrange(10)) + str(index).zfill(4)[:4]
    role = "BUSINESS"
    regip = "0:0:0:0:0:0:0:1"
    bis_company = row[4]
    bis_ceo = row[5]
    bis_openDate = row[6]
    bis_bizRegNum = row[7].replace("-", "")[: 4] + str(randrange(1000000))
    bis_zip = row[9]
    bis_addr = row[10]
    bis_addrDetail = row[11]

    userId_id_list.append(user_id)

    userInfo_values = []
    userInfo_values.insert(0, "'" + user_id + "'")
    userInfo_values.insert(1, "'" + hp + "'")
    userInfo_values.insert(2, "'" + nick + "'")
    userInfo_values.insert(3, "'" + type + "'")
    userInfo_values.insert(4, "'" + role + "'")
    userInfo_values.insert(5, "'" + regip + "'")
    userInfoList.append('({})'.format(','.join(userInfo_values)))

    user_vlaues = []
    user_vlaues.insert(0, "'" + user_id + "'")
    user_vlaues.insert(1, "'" + "1234" + "'")
    userList.append('({})'.format(','.join(user_vlaues)))

    businessInfoList_vlaues = []
    businessInfoList_vlaues.insert(0, "'" + user_id + "'")
    businessInfoList_vlaues.insert(1, "'" + bis_company + "'")
    businessInfoList_vlaues.insert(2, "'" + bis_ceo + "'")
    businessInfoList_vlaues.insert(3, "'" + bis_openDate + "'")
    businessInfoList_vlaues.insert(4, "'" + bis_bizRegNum + "'")
    businessInfoList_vlaues.insert(5, "'" + hp + "'")
    businessInfoList_vlaues.insert(6, "'" + bis_zip + "'")
    businessInfoList_vlaues.insert(7, "'" + bis_addr + "'")
    businessInfoList_vlaues.insert(8, "'" + bis_addrDetail + "'")
    businessInfoList.append('({})'.format(','.join(businessInfoList_vlaues)))
    
userInfo_sql = userInfo_sql + ','.join(userInfoList)
user_sql = user_sql + ','.join(userList)
businessInfo_sql = businessInfo_sql + ','.join(businessInfoList)

# SQL 실행
cur.execute(userInfo_sql)
conn.commit()
cur.execute(user_sql)
conn.commit()
cur.execute(businessInfo_sql)
conn.commit()

# 3. 불러온 Workbook의 sheet확인
accommodation = wb['숙소']

rows = accommodation['A2':'P4557']

rowsList = []

for row in rows:
    rowList = []
    for cell in  row:
        rowList.append(str(cell.value).replace("'", ""))
    rowsList.append(rowList)

# lemo_product_accommodation(숙소) INSERT SQL문
acc_sql = "INSERT INTO `lemo_product_accommodation` (`acc_id`, `user_id`, `acc_name`, `accType_no`, `province_no`, `acc_city`, "
acc_sql = acc_sql + "`acc_zip`, `acc_addr`, `acc_addrDetail`, `acc_longtitude`, `acc_lattitude`, `acc_xy`, `acc_info`, `acc_comment`," 
acc_sql = acc_sql + "`acc_thumbs`, `acc_checkIn`, `acc_checkOut`) VALUES"

accList = []
for index, row in enumerate(rowsList):
    acc_id = row[0]
    userId_id = userId_id_list[index]
    acc_name = row[2]
    accType_no = row[3]
    province_no = row[4]
    acc_city = row[5]
    acc_zip = row[6]
    acc_addr = row[7]
    acc_addrDetail = row[8]
    acc_longtitude = row[9]
    acc_lattitude = row[10]
    acc_xy = "ST_GeomFromText('POINT({} {})')".format(acc_longtitude, acc_lattitude)
    acc_info = "내용없음" if row[11] == None else row[11]
    acc_comment = row[12]
    acc_thumbs = row[13]
    acc_checkIn = row[14]
    acc_checkOut = row[15]

    accList_vlaues = []
    accList_vlaues.insert(0, "'" + acc_id + "'")
    accList_vlaues.insert(1, "'" + userId_id + "'")
    accList_vlaues.insert(2, "'" + acc_name + "'")
    accList_vlaues.insert(3, "'" + accType_no + "'")
    accList_vlaues.insert(4, "'" + province_no + "'")
    accList_vlaues.insert(5, "'" + acc_city + "'")
    accList_vlaues.insert(6, "'" + acc_zip + "'")
    accList_vlaues.insert(7, "'" + acc_addr + "'")
    accList_vlaues.insert(8, "'" + acc_addrDetail + "'")
    accList_vlaues.insert(9, "'" + acc_longtitude + "'")
    accList_vlaues.insert(10, "'" + acc_lattitude + "'")
    accList_vlaues.insert(11, acc_xy)
    accList_vlaues.insert(12, "'" + acc_info + "'")
    accList_vlaues.insert(13, "'" + acc_comment + "'")
    accList_vlaues.insert(14, "'" + acc_thumbs + "'")
    accList_vlaues.insert(15, "'" + acc_checkIn + "'")
    accList_vlaues.insert(16, "'" + acc_checkOut + "'")

    accList.append('({})'.format(','.join(accList_vlaues)))

acc_sql = acc_sql + ','.join(accList)

# SQL 실행
cur.execute(acc_sql)
conn.commit()

# 3. 불러온 Workbook의 sheet확인
accommodation = wb['객실']

rows = accommodation['A2':'I38007']

rowsList = []

for row in rows:
    rowList = []
    for cell in  row:
        rowList.append(str(cell.value).replace("'", ""))
    rowsList.append(rowList)

# lemo_product_room(객실) INSERT SQL문
room_sql = "INSERT INTO `lemo_product_room` (`room_id`, `acc_id`, `room_name`, `room_stock`, `room_price`, `room_info`, "
room_sql = room_sql + "`room_thumb`, `room_checkIn`, `room_checkOut`) VALUES"

roomList = []
for index, row in enumerate(rowsList):
    room_id = row[0]
    acc_id = row[1]
    room_name = row[2]
    room_stock = str(row[3])
    room_price = str(row[4])
    room_info = row[5]
    room_thumb = row[6]
    room_checkIn = row[7]
    room_checkOut = row[8]

    roomList_vlaues = []
    roomList_vlaues.insert(0, "'" + room_id + "'")
    roomList_vlaues.insert(1, "'" + acc_id + "'")
    roomList_vlaues.insert(2, "'" + room_name + "'")
    roomList_vlaues.insert(3, "'" + room_stock + "'")
    roomList_vlaues.insert(4, "'" + room_price + "'")
    roomList_vlaues.insert(5, "'" + room_info + "'")
    roomList_vlaues.insert(6, "'" + room_thumb + "'")
    roomList_vlaues.insert(7, "'" + room_checkIn + "'")
    roomList_vlaues.insert(8, "'" + room_checkOut + "'")

    roomList.append('({})'.format(','.join(roomList_vlaues)))

room_sql = room_sql + ','.join(roomList)

# SQL 실행
cur.execute(room_sql)
conn.commit()

# 데이터베이스 종료
cur.close()