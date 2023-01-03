"""
날짜 : 2023/01/03
이름 : 서정현
번호 : 9498
내용 : 시험 성적
"""

score = int(input())

if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else :
    print('F')

