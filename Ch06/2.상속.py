"""
날짜 : 2023/01/11
이름 : 서정현
내용 : 파이썬 상속 실습하기
"""

from sub1.StockAccount import StockAccount


kb = StockAccount("KB증권", "101-12-1234", "홍길동", 50000, "삼성전자", 10, 60000)
kb.deposite(500000)
kb.sell(5, 1000)
kb.show()