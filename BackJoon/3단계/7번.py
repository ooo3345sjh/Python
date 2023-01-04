"""
날짜 : 2023/01/04
이름 : 서정현
번호 : 11022
내용 : A+B - 8
"""
import sys

num = int(input())

i = 1
while i <= num:
    a, b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d' % (i, a, b, a + b))
    i += 1
