"""
날짜 : 2023/01/03
이름 : 서정현
번호 : 1330
내용 : 두 수 비교하기 
"""

a, b = map(int, input().split())

if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')
