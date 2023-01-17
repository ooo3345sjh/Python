"""
날짜 : 2023/01/13
이름 : 서정현
내용 : 파이썬 사용자 관리 프로그래밍 실습
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1', 
                        user='root', 
                        password='1234', 
                        db='java2db', 
                        charset='utf8')

while True:
    print()
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))
    except:
        print('숫자를 입력하세요.')
        continue
    
    if answer == 0:
        break

    elif answer == 1:
        print('회원 등록...')
        
        cur = conn.cursor()
        
        uid = input('아이디 입력 : ')
        name = input('이름 입력 : ')
        hp = input('휴대폰 입력 : ')
        age = input('나이 입력 : ')

        result = cur.execute("INSERT INTO `user3` VALUES('%s', '%s', '%s', '%s')" % (uid, name, hp, age))
        conn.commit()
        cur.close()

    elif answer == 2:
        print('회원 조회...')

        cur = conn.cursor()
    
        cur.execute("SELECT * FROM `user3`")
        conn.commit()
        
        users = cur.fetchall()
        
        if len(users) == 0:
            print('현재 회원이 없습니다.')

        for user in users:
            print('-------------------------------')
            print('|%s|%s|%s|%s|' % (user[0], user[1], user[2], user[3]))
        cur.close()

    elif answer == 3:

        print('회원 검색...')

        cur = conn.cursor()
    
        uid = input('검색 아이디 입력 : ')
        cur.execute("SELECT * FROM `user3` WHERE `uid`='%s'" % (uid))
        conn.commit()

        users = cur.fetchall()

        if len(users) == 0:
            print('검색된 회원이 없습니다.')

        for user in users:
            print('아이디 :', user[0])
            print('이름 :', user[1])
            print('휴대폰 :', user[2])
            print('나이 :', user[3])

        cur.close()

    elif answer == 4:

        print('회원 삭제...')
        cur = conn.cursor()
    
        uid = input('삭제 아이디 입력 : ')
        result = cur.execute("DELETE FROM `user3` WHERE `uid`='%s'" % (uid))
        conn.commit()

        if result == 0:
            print('삭제된 회원이 없습니다.')
        cur.close()

    else:
        print('0 ~ 4중에서 입력하세요.')


# 데이터베이스 종료
conn.close()
print('프로그램 종료...')