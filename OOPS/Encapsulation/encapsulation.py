class Account:
    def __init__(self,ac,name,balance,bank_name):
        self.account_number=ac
        self.holder_name=name
        self._bank_name=bank_name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance

    @property
    def bank_name(self):
        return self._bank_name


ac=Account(123,'anil',20000,'sbi')
print(ac.account_number)
print(ac.holder_name)
print(ac.bank_name)
print(ac.get_balance())