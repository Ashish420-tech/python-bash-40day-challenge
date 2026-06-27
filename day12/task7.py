class Bank:

    def __init__(self,balance):
        self.__balance=balance

    def show(self):
        print(self.__balance)

b=Bank(5000)

b.show()

