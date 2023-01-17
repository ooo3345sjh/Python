"""
날짜 : 2023/01/11
이름 : 서정현
내용 : 파이썬 클래스 실습하기
"""
from sub1.Car import Car
from sub1.Account import Account

sonata = Car("sonata", "red", 1000)
sonata.speedUp()
sonata.speedDown()
sonata.show()

bmw = Car("BMW", "blue", 4000)
bmw.speedUp()
bmw.speedDown()
bmw.show()

kb = Account("국민은행", "101-12-1234", "김유신", 30000)
kb.deposite(5000)
kb.withdraw(3000)
kb.show()

hana = Account("하나은행", "131-22-1234", "김춘추", 20000)
hana.deposite(5000)
hana.withdraw(3000)
hana.show()
hana._balance -= 1
print(hana._balance)

