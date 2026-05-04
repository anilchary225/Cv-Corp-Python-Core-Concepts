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

class A:
    def method(self):
        print('A.method')
    def method2(self):
        print('A.method2')
class B(A):
    def method(self):
        print('B.method')
        super().method2()
    def method2(self):
        print('B.method2')
        super().method()
obj=B()
obj.method()


'''Create a base class Animal with a method sound(). Create a derived class Dog
that overrides the sound() method. Demonstrate method overriding.'''


'''• Create class A with method show(). Create class B(A) that overrides show() and
also calls the parent method using super().'''


'''• Create multi-level inheritance with classes A → B → C, each having a method
display() printing the class name. Create object of C and call display(),
showing method resolution.'''


'''• Implement hierarchical inheritance using a base class Vehicle and two child
classes Car and Bike, each defining a method wheels().'''


'''• Create class Employee with an instance method salary(). Create class
Manager(Employee) that overrides salary() and adds an incentive. Demonstrate
both outputs.'''


'''• Create class University with a class variable and a class method. Inherit it
into class College and access the parent’s class variable from the child class.'''


'''• Create class MathOps with a static method add(a, b). Create class
AdvancedOps(MathOps) and use the static method without overriding it.'''


'''• Create two classes Father and Mother, both defining a method skills(). Create
class Child(Father, Mother) and check which skills() runs using MRO.'''


'''• Create an abstract class Shape with an abstract method area(). Create class
Rectangle(Shape) that implements the area() method.'''


'''• Create class Person with a constructor __init__(name). Create class
Student(Person) with constructor __init__(name, roll). Use super() to call the
parent constructor.'''