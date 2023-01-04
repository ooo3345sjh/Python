"""
날짜 : 2023/01/04
이름 : 서정현
번호 : 2439
내용 : 별 찍기 - 2
"""
num = int(input())

i = 1
while num > 0 :
    print(' ' * (num - 1), end='')
    print('*' * i)
    num -= 1
    i += 1
