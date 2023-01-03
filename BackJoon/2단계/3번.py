"""
날짜 : 2023/01/03
이름 : 서정현
번호 : 2753
내용 : 윤년
"""

year = int(input())

if (year % 4 == 0 and not(year % 100 == 0)) or year%400 == 0:
    print('1')
else :
    print('0')

