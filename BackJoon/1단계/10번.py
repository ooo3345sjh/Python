"""
날짜 : 2023/01/02
이름 : 서정현
번호 : 10430
내용 : 나머지
"""

A, B, C = map(int, input().split())

print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep='\n')
