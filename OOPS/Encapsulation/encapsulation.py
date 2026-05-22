# class Account:
#     def __init__(self,ac,name,balance,bank_name):
#         self.account_number=ac
#         self.holder_name=name
#         self._bank_name=bank_name
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def get_balance(self):
#         return self.__balance
#
#     @property
#     def bank_name(self):
#         return self._bank_name
#
#
# ac=Account(123,'anil',20000,'sbi')
# print(ac.account_number)
# print(ac.holder_name)
# print(ac.bank_name)
# print(ac.get_balance())


'''
1. Create a BankAccount class that stores:
• account number
• balance (should not be directly modifiable)
You must:
1. 2. 3. 4. Make the balance attribute inaccessible from outside.
Provide functions to deposit/withdraw that validate the amount.
Prevent withdrawal if balance becomes negative.
Show what happens if someone tries to modify balance directly and why
encapsulation prevents it.
'''

class BankAccount:
    def __init__(self,name,ac_no,balance):
        self.name=name
        self._ac_no=ac_no
        self.__balance=balance
    def deposit(self,amount):  #setter
        self.__balance+=amount
    def withdraw(self,withdraw_amount): #setter
        if self.__balance - withdraw_amount > 0:
            self.__balance-=withdraw_amount
    @property  #name masking : converting the method into variable
    def get_balance(self):
        print(f'{self.name} is trying to check the balance')
        return self.__balance
    @get_balance.setter #updating the variable by using setter
    def balance(self,new_amount):
        self.__balance=new_amount
h1=BankAccount('Siddu',12345,10000000)
print(h1._BankAccount__balance) #but we should not access this like
print(h1.get_balance)
h1.balance=2000000  #assigning the value to a variable
print(h1.get_balance)
h1.deposit(2000000)
print(h1.get_balance)
h1.withdraw(45000)
print(h1.get_balance)