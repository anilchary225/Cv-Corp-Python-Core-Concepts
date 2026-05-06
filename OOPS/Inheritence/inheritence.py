# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bunk(self,a):
#         print('I am bunking class')
# class CVStudent(Student):
#     def __init__(self, name, age,batch):
#         super().__init__(name, age)
#         self.batch = batch
#     def bunk(self):
#         super().bunk(3)
#         print(f'I am bunking class {self.batch}')
# s1=CVStudent("Pranav",22,"python 7")
# s1.bunk()
# print(CVStudent.mro())



# class A:
#     def __init__(self):
#         print('A')
# class B(A):
#     def __init__(self,a,b):
#         print('B')
#         self.a = a
#         super().__init__(b)
#
# class C(A):
#     def __init__(self,b):
#         print('C')
#         self.b = b
#         super().__init__()
#
# class D(B,C):
#     def __init__(self,a,b):
#         print('D')
#         super().__init__(a,b)
#
# obj=D(1,2)
# print(obj.a)
# print(obj.b)

# class A:
#     def method(self):
#         print('A.method')
#     def method2(self):
#         print('A.method2')
# class B(A):
#     def method(self):
#         print('B.method')
#         super().method2()
#     def method2(self):
#         print('B.method2')
#         super().method()
# obj=B()
# obj.method()


'''Create a base class Animal with a method sound(). Create a derived class Dog
that overrides the sound() method. Demonstrate method overriding.'''

# class Animal:
#     def sound(self):
#         print('Animal Sound')
# class Dog(Animal):
#     def sound(self):
#         print('Dog Sound')
#
# d=Dog()
# d.sound()

'''• Create class A with method show(). Create class B(A) that overrides show() and
also calls the parent method using super().'''

# class A:
#     def show(self):
#         print('Class A')
# class B(A):
#     def show(self):
#         print('Class B')
#         super().show()
# b=B()
# b.show()

'''• Create multi-level inheritance with classes A → B → C, each having a method
display() printing the class name. Create object of C and call display(),
showing method resolution.'''


# class A:
#     def display(self):
#         print('Class A')
# class B(A):
#     def display(self):
#         super().display()
#         print('Class B')
# class C(B):
#     def display(self):
#         super().display()
#         print('Class C')
# c=C()
# c.display()

'''• Implement hierarchical inheritance using a base class Vehicle and two child
classes Car and Bike, each defining a method wheels().'''

# class Vehicle:
#     def start(self):
#         print('Starts engine')
#
# class Bike(Vehicle):
#     def wheels(self):
#         super().start()
#         print('This vehicle has 2 wheels')
# class Car(Vehicle):
#     def wheels(self):
#         super().start()
#         print('This vehicle has 4 wheels')
#
# Bike().wheels()
# Car().wheels()

'''• Create class Employee with an instance method salary(). Create class
Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
both outputs.'''

# class Employee:
#     def __init__(self,s,i):
#         self.salary=s
#         self.incentives=i
#     def show_salary(self):
#         print('Employee salary: ',self.salary)
# class Manager(Employee):
#     def __init__(self,s,i):
#         super().__init__(s,i)
#     def show_salary(self):
#         total=self.salary + self.incentives
#         super().show_salary()
#         print('Manager Salary (with incentives): ',total)
#
# emp=Employee(40000,3000)
# emp.show_salary()
# ma=Manager(50000,3000)
# ma.show_salary()




'''• Create class University with a class variable and a class method. Inherit it
into class College and access the parent’s class variable from the child class.'''


# class University:
#     university_name='JNTU'
#     @classmethod
#     def show_university(cls):
#         print(cls.university_name)
# class College(University):
#     @classmethod
#     def show_university(cls):
#         super().show_university()
# u=College()
# u.show_university()

'''• Create class MathOps with a static method add(a, b). Create class
AdvancedOps(MathOps) and use the static method without overriding it.'''


# class MathOps:
#     @staticmethod
#     def add(a,b):
#         return a+b
# class AdvancedOps(MathOps):
#     @staticmethod
#     def show_add(a,b):
#         print(MathOps.add(a,b))  #if u take super() instead of MathOps we get error
#
'''
        👉 Why this fails:

            * super() needs a class or instance context
            * @staticmethod has no self or cls
            * So Python doesn’t know which class to refer to → ❌ error
'''
#
# AdvancedOps().show_add(1,5)


'''• Create two classes Father and Mother, both defining a method skills(). Create
class Child(Father, Mother) and check which skills() runs using MRO.'''


# class Father:
#     def skills(self):
#         print('skills from Father')
# class Mother:
#     def skills(self):
#         print('Skills from Mother')
#
# class Child(Father, Mother):
#     def show_skills(self):
#         super().skills()
# Child().show_skills()
# print(Child.mro())

# o/t:
# skills from Father
# [<class '__main__.Child'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>]

'''• Create an abstract class Shape with an abstract method area(). Create class
Rectangle(Shape) that implements the area() method.'''



'''• Create class Person with a constructor __init__(name). Create class
Student(Person) with constructor __init__(name, roll). Use super() to call the
parent constructor.'''

# class Person:
#     def __init__(self,n):
#         self.name=n
# class Student(Person):
#     def __init__(self,name,r):
#         super().__init__(name)
#         self.roll_no=r
#     def display(self):
#         print('Person name: ',self.name,'\nStudent Roll no: ',self.roll_no)
# s1=Student('anil',7)
# s1.display()

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