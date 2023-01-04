"""
날짜 : 2023/01/04
이름 : 서정현
번호 : 15552
내용 : 빠른 A+B 
"""
import sys

num = int(input())

i = 1
while i <= num:
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    i += 1
