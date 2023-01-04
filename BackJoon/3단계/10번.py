"""
날짜 : 2023/01/04
이름 : 서정현
번호 : 10952
내용 : A+B - 5
"""
import sys

while True :
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break

    print(a + b)
