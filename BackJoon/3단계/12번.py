"""
날짜 : 2023/01/04
이름 : 서정현
번호 : 1110
내용 : 더하기 사이클
"""
import sys
num = int(sys.stdin.readline())

oriValue = num 
i = 1
while True:
    n1 = num // 10
    n2 = num % 10
    n3 = (n1 + n2) % 10
    num = int(str(n2) + str(n3))
    
    if num == oriValue: 
        break
    i += 1

print(i)

