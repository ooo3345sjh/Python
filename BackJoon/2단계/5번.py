"""
날짜 : 2023/01/03
이름 : 서정현
번호 : 2884
내용 : 알람 시계
"""

a, b = map(int, input().split())


if a == 0 and b < 45:
    print('%d %d' % (23, 60 + (b-45)))
elif b<45:
    print('%d %d' % (a - 1, 60 + (b-45)))
else :
    print('%d %d' % (a, b-45))

