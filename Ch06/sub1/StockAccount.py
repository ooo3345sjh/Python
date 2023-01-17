from sub1.Account import Account

class StockAccount(Account) :
    def __init__(self, bank, id, name, balance, stock, amount, price):
        super().__init__(bank, id, name, balance)

        self.__stock = stock
        self.__amount = amount
        self.__price = price

    def sell(self, amount, price):
        self._balance += amount * price
        self.__amount -= amount

    def buy(self, amount, price):
        self._balance -= amount * price
        self.__amount += amount

    def show(self):
        super().show()
        print('주식종목 :', self.__stock)
        print('주식수량 :', self.__amount)
        print('주식가격 :', self.__price)