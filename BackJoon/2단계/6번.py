"""
날짜 : 2023/01/03
이름 : 서정현
번호 : 2525
내용 : 오븐 시계
"""

A, B = map(int, input().split())
C = int(input())

B = B+C 
A = (A + B//60)%24 # 몫
B %= 60 # 나머지
    
print('%d %d' % (A, B))
