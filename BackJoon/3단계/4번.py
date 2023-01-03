"""
날짜 : 2023/01/03
이름 : 서정현
번호 : 25304
내용 : 영수증 
"""

total = int(input())
count = int(input())
sum = 0

for i in range(count):
    a, b = map(int, input().split())
    sum = sum + (a * b)

total = 'Yes' if total == sum else 'No'

print(total)
