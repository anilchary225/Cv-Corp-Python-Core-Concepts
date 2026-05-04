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