'''
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── ArithmeticError
      │     ├── FloatingPointError
      │     ├── OverflowError
      │     └── ZeroDivisionError
      │
      ├── AssertionError
      │
      ├── AttributeError
      │
      ├── BufferError
      │
      ├── EOFError
      │
      ├── ImportError
      │     └── ModuleNotFoundError
      │
      ├── LookupError
      │     ├── IndexError
      │     └── KeyError
      │
      ├── MemoryError
      │
      ├── NameError
      │     └── UnboundLocalError
      │
      ├── OSError
      │     ├── BlockingIOError
      │     ├── ChildProcessError
      │     ├── ConnectionError
      │     │     ├── BrokenPipeError
      │     │     ├── ConnectionAbortedError
      │     │     ├── ConnectionRefusedError
      │     │     └── ConnectionResetError
      │     ├── FileExistsError
      │     ├── FileNotFoundError
      │     ├── InterruptedError
      │     ├── IsADirectoryError
      │     ├── NotADirectoryError
      │     ├── PermissionError
      │     ├── ProcessLookupError
      │     └── TimeoutError
      │
      ├── ReferenceError
      │
      ├── RuntimeError
      │     ├── NotImplementedError
      │     └── RecursionError
      │
      ├── StopIteration
      │
      ├── StopAsyncIteration
      │
      ├── SyntaxError
      │     └── IndentationError
      │           └── TabError
      │
      ├── SystemError
      │
      ├── TypeError
      │
      ├── ValueError
      │     └── UnicodeError
      │           ├── UnicodeDecodeError
      │           ├── UnicodeEncodeError
      │           └── UnicodeTranslateError
      │
      └── Warning
            ├── DeprecationWarning
            ├── PendingDeprecationWarning
            ├── RuntimeWarning
            ├── SyntaxWarning
            ├── UserWarning
            ├── FutureWarning
            ├── ImportWarning
            ├── UnicodeWarning
            └── ResourceWarning
'''


# try:
#     print("5"+5)
#     print("end")
# except TypeError as te:
#     print(te)
# else:
#     print("something in else")
# finally:
#     print("finally")


# obj= TypeError("creating error")
# # raise obj # custom exception case
# try:
#     password=input("enter password")
#     if len(password)<8:
#         raise ValueError("password is too short")
#     else:
#         print("password created")
# except ValueError as ve:
#     print(ve)
#
#
# class A:
#     def m1(self):
#         raise NotImplementedError("implement m1 method")
# class B(A):
#    def m1(self):
#        print("m1")
# obj=B()
# obj.m1()

# custom exception class
# class Python78Error(Exception):
#     pass

# obj=Python78Error("testing 7-8 error")
# raise obj

# bank account -> name, age, pancard
# if age of the person is less than 18 create an error
# "InvalidAgeError" create the object
# create the object only when there is no error
'''custom exception'''

# class InvalidAgeError(Exception):
#     pass
#
# class BankAccount:
#     def __init__(self,name,age,pancard):
#         self.name=name
#         self.pancard=pancard
#         if age<18:
#             raise InvalidAgeError()
#         else:
#             self.age=age
# obj=BankAccount("John",17,"Pancard")
# print(obj.age)


# def fun(a):
#     try:
#         if a==5:
#             raise TypeError("Testing")
#         else:
#             print(a)
#     except TypeError as e:
#         print(e)
#
# for i in range(10):
#     ####
#     fun(i)
#     ##


# try
# except
# else
# finally
# raise:
#     Custom Exception:
#         - pre defined class error object
#         - custom error class error object

# try:
#     print("5"+5)
#     print("end")
# except TypeError as te:
#     print(te)
# else:
#     print("something in else")
# finally:
#     print("finally")
#
#
# # obj= TypeError("creating error")
# # raise obj # custom exception case
# try:
#     password=input("enter password")
#     if len(password)<8:
#         raise ValueError("password is too short")
#     else:
#         print("password created")
# except ValueError as ve:
#     print(ve)
from email.errors import MessageError


# class A:
#     def m1(self):
#         raise NotImplementedError("implement m1 method")
# class B(A):
#    def m1(self):
#        print("m1")
# obj=B()
# obj.m1()
#
# # custom exception class
# class Python78Error(Exception):
#     pass

# obj=Python78Error("testing 7-8 error")
# raise obj

# bank account -> name, age, pancard
# if age of the person is less than 18 create an error
# "InvalidAgeError" create the object
# create the object only when there is no error
# class InvalidAgeError(Exception):
#     pass
#
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         if age<0:
#             raise ValueError("invalid age")
#         else:
#             self.age=age
# try:
#     obj=Person("John",-5)
#     print(obj.age)
# except ValueError as e:
#     print(e)


# def fun(a):
#     try:
#         if a==5:
#             raise TypeError("user name already exists")
#         else:
#             print(a)
#     except TypeError as e:
#         raise Python78Error(f"Profile Service: {e}")
# try:
#     for i in range(10):
#         try:
#             fun(i)
#         except Python78Error as e:
#             raise Python78Error(f"ProfilePage: {e}")
# except Python78Error as e:
#     print(f"Instagram: {e}")




# try
# except
# else
# finally
# raise:
#     Custom Exception:
#         - pre defined class error object
#         - custom error class error object
# Error Chaining





'''
• Create a class Person whose constructor takes age as an argument. Raise a
ValueError if the age is less than 0.
'''

# class Person:
#     def __init__(self,age):
#         if age<0:
#             raise ValueError('age must be greater than 0')
#         else:
#             self.age=age
# try:
#     obj=Person(-1)
#     print(obj.age)
# except ValueError as ve:
#     print(ve)
'''

• Write a function named find_length(obj) that uses a loop to calculate the
length of the given object without using the built-in len() function. The
function should return the calculated length if the object is iterable. If a
non-iterable object such as an integer is passed, the function should raise and
handle a TypeError, and print an appropriate error message explaining what
happens when an integer is sent as input.
'''

# class C:
#     pass
# print(isinstance(obj, C))

# l=[1,2,3,4,5,6]
# c=0

# d={"A":1,"B":2,"C":3}
# for i,j in d.items():
#     c+=1
# for i in l:
#     c+=1
# print(c)
# def find_len(v):
#     c=0
#     if isinstance(v, (str, dict, set, list, tuple)):
#         for i in v:
#             c+=1
#         return c
#     else:
#         raise TypeError(f"cannot find value for {type(v)} type data")
# print(find_len(d))
# print(find_len([1,2,3]))       # 3
# print(find_len("python"))      # 6
# print(find_len((1,2,3,4)))     # 4
# print(find_len({"A":1,"B":2})) # 2
# print(find_len(100))           # TypeError

'''

• Create a class Student with an attribute marks. Implement a method
set_marks(marks) that raises a ValueError if marks are not in the range 0 to
100.

'''
# class Student:
#     def set_marks(self,marks):
#         try:
#             if marks < 0 or marks > 100 :
#                 raise ValueError('Marks should be in between 0 to 100')
#             else:
#                 self.marks=marks
#         except ValueError as ve:
#             print(ve)
# s1=Student()
# s1.set_marks(1000)
# print(s1.marks)




'''


• Create a custom exception named InvalidAgeError. Create a class Voter with a
method check_eligibility(age) that raises this exception if age is less than 18.

'''
# class InvalidAgeError(Exception):
#     pass
#
# class Voter:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def age_eligibility(self):
#         try:
#             if self.age < 18:
#                 raise InvalidAgeError('Age must be greater than 18')
#             else:
#                 print('this person is eligible')
#         except InvalidAgeError as age_error:
#             print(age_error)
# v1=Voter('Anil',1)
# v1.age_eligibility()



'''

• Create a class BankAccount with an attribute balance. Implement a method
withdraw(amount) that raises an exception if the withdrawal amount is greater
than the available balance.

'''
# class BalanceError(Exception):
#     pass
#
# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def withdraw(self,amount):
#         try:
#             if amount>self.balance:
#                 raise BalanceError('inSufficient Balance')
#             else:
#                 self.balance-=amount
#         except BalanceError as be:
#             print(be)
#
# b1=BankAccount(200000)
# b1.withdraw(2000)
# print(b1.balance)

'''

• Create a class PasswordValidator with a method validate(password). Raise an
exception if the password length is less than 8 characters.

'''
# class PasswordValidationError(Exception):
#     pass
#
# class PasswordValidator:
#     def validate(self,password):
#         try:
#             if len(password) < 8 :
#                 raise PasswordValidationError('Password must be greater than 8 characters')
#             else:
#                 self.password=password
#         except PasswordValidationError as pve:
#             print(pve)
# pv=PasswordValidator()
# pv.validate('dhjdsj')
# print(pv.password)

'''


• Create a class UserInput with a method get_integer(value). Handle ValueError
and TypeError using separate except blocks.
'''
# class UserInput:
#
#     def get_integer(self, value):
#
#         try:
#             return int(value)
#
#         except ValueError as ve:
#             print("ValueError:", ve)
#
#         except TypeError as te:
#             print("TypeError:", te)
#
#
# u = UserInput()
#
# print(u.get_integer("123"))   # valid
# print(u.get_integer("abc"))   # ValueError
# print(u.get_integer(None))    # TypeError

'''
• Create a base class Shape with a method area() that raises
NotImplementedError. Create a child class Rectangle that overrides and
implements the area method.

'''
# class Shape:
#     def area(self):
#         raise NotImplementedError('Implement area method')
# class Rectangle(Shape):
#     pass
#
# Rectangle().area()


'''


• Create a class Service with a method that calls another method which raises an
exception. Catch and handle the exception in the Service class.
'''
# class Service:
#     def divide(self,a,b):
#         return a/b
#     def process(self):
#         try:
#             result=self.divide(10,0)
#             print(result)
#         except ZeroDivisionError as ze:
#             print('Exception handled: ',ze)
# s=Service()
# s.process()

'''
• Create a class Transaction with a method process() that uses try, except, and
finally blocks to ensure a cleanup message is always printed.
'''
# class TransactionError(Exception):
#     pass
# class Transaction:
#     def process(self,amount):
#         try:
#             if amount>0:
#                 print('Transaction done')
#             else:
#                 raise TransactionError('amount should be greater than 0,Transaction failed')
#         except TransactionError as te:
#             print(te)
#         finally:
#             print('Transaction closed')
# t=Transaction()
# t.process(1000)
# t.process(-1000)
'''
• Create a class LoginSystem with a method login(password) that raises an
exception for an incorrect password and handles the exception outside the class.
'''

# class PasswordError(Exception):
#     pass
#
# class LoginSystem:
#     def login(self,password):
#         if password!='password':
#             raise PasswordError('Incorrect Password')
# try:
#     password=input()
#     LoginSystem().login(password)
# except PasswordError as pe:
#     print(pe)