'''
Q1. Create a class Animal with make_sound() and derived classes Dog, Cat, Cow that
override it.
Demonstrate polymorphism by iterating over a list of different animal objects and calling
make_sound().
'''
# class Animal:
#     def make_sound(self):
#         print('Animal Sound')
# class Dog(Animal):
#     def make_sound(self):
#         print('Dog Sound')
# class Cat(Animal):
#     def make_sound(self):
#         print('Cat Sound')
# class Cow(Animal):
#     def make_sound(self):
#         print('Cow Sound')
# def sound(animal):
#     animal.make_sound()
# l=[
#     Animal(),
#     Dog(),
#     Cat(),
#     Cow()
# ]
# for i in l:
#     sound(i)


'''
Q2. Write a function operate(device) that calls device.start().
Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
method, but share no inheritance relationship.
Show that Python’s polymorphism works through behavior, not type.
'''


# class Car:
#     def start(self):
#         print('Car')
# class Computer:
#     def start(self):
#         print('Computer')
# class WashingMachine:
#     def start(self):
#         print('WashingMachine')
#
# l=[Car(),Computer(),WashingMachine()]
# def operate(device):
#     device.start()
# for i in l:
#     operate(i)

'''
Q3. Create a Vector class that supports:
• + operator → add coordinates
• == operator → compare equality
Show how operator overloading gives natural polymorphism to user-defined classes.
'''

# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,o2):
#         return Vector(self.x+o2.x,self.y+o2.y)
#     def __eq__(self, o2):
#         return self.x==o2.x and self.y==o2.y
#
#     # for printing object
#     def __str__(self):
#         return f'Vector({self.x},{self.y})'
# v1=Vector(2,3)
# v2=Vector(3,4)
# v3=Vector(1,1)
# print(v1+v2+v3)
# print(v1==v2)

'''
Q4. Create a base class Transport with move() and derived classes Bus and Bike that
override it but also call the parent implementation using super().
Show the combination of reuse + custom behavior.
'''
# class Transport:
#     def move(self):
#         print('Transport')
# class Bus(Transport):
#     def move(self):
#         super().move()
#         print('Bus is moving')
# class Bike(Transport):
#     def move(self):
#         super().move()
#         print('Bike is moving')
# Bike().move()
# Bus().move()


'''
Q5. Using the abc module, create an abstract class Notification with send().
Implement subclasses EmailNotification, SMSNotification, PushNotification — each
with its own send() logic.
Demonstrate polymorphism by looping over all and calling send().
'''

'''
Q6. Design:
• Base class Payment with process(amount)
• Subclass CreditCardPayment adds process(amount, card_type)
Demonstrate what happens when overriding with different signatures and how Python
handles it.
'''
#
# class Payment:
#     def process(self,amount):
#         print(f'Processing payment of {amount}')
# class CreditCardPayment(Payment):
#     def process(self,amount,card_type):
#         super().process(amount)
#         print(f'Processing {amount} using {card_type} credit card')
#
# cc=CreditCardPayment()
#
# cc.process(2000,'VISA')

'''
Q7. Create:
• Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
each implementing a different logic method.
Demonstrate how polymorphism can be achieved without inheritance by using
interchangeable strategy objects.
'''
# class BB:
#     def logic(self,data):
#         print('Bubble Sort: ',sorted(data))
# class MS:
#     def logic(self,data):
#         print('Merge Sort: ',sorted(data))
# class QS:
#     def logic(self,data):
#         print('Quick Sort: ',sorted(data))
# class Sorter:
#     def change(self,strategy,data):
#         strategy.logic(data)
# num=[2,3,4,5,6]
# l=[BB(),MS(),QS()]
# for i in l:
#     Sorter().change(i,num)

'''
Q8. Create:
• Base Account → withdraw()
• Subclass SavingsAccount → modifies withdraw()
• Subclass PremiumSavingsAccount → overrides again but calls parent using super()
Show how polymorphism works across multiple levels.
'''
# class Account:
#     def __init__(self,amount):
#         self.amount = amount
#
#     def withdraw(self):
#         print('Withdrawing amount ',self.amount)
#
# class SavingsAccount(Account):
#
#     def withdraw(self, money):
#
#         self.amount-=money
#         print('Remaining Balance: ',self.amount)
# class PremiumSavingsAccount(Account):
#     def withdraw(self):
#         super().withdraw()
#
# pr=PremiumSavingsAccount(15000)
# pr.withdraw()
# saa=SavingsAccount(100000)
# saa.withdraw(20000)

'''
Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
Rectangle,
each implementing a draw() method.
Add another unrelated class Car with draw() and pass it — what happens and why?
'''

# class Circle:
#     def draw(self):
#         print('Circle drawn')
# class Square:
#     def draw(self):
#         print('Square drawn')
# class Rectangle:
#     def draw(self):
#         print('Rectangle Drawn')
# class Car:
#     def draw(self):
#         pass
# l=[Circle(),Square(),Rectangle()]
# def draw(shape):
#     shape.draw()
# for i in l:
#     draw(i)
# Car().draw()


'''
Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
pay() method.
Now implement a version that checks types explicitly using isinstance() before calling
pay().
Compare both designs and explain why one breaks the spirit of polymorphism.
'''

# class UPI:
#     def pay(self):
#         print('Pay through UPI')
# class Card:
#     def pay(self):
#         print('Pay through Card')
# class Cash:
#     def pay(self):
#         print('Pay through Cash')
# def make_payment(method):
#     if isinstance(method, UPI):
#         method.pay()
#     elif isinstance(method,Card):
#         method.pay()
#     elif isinstance(method,Cash):
#         method.pay()
#     else:
#         print('Invalid Payment type')
# l=[UPI(),Card(),Cash()]
# for i in l:
#     make_payment(i)