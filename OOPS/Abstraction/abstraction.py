from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         print("A")
# class B(A):
#     @abstractmethod
#     def m2(self):
#         print("B")
# class C(A):
#     def m1(self):
#         print("C")
# obj=A()
# obj.m1()

#  Create:
# • Abstract class VehicleControl with methods accelerate(),
# brake(), steer()
# • Implement CarControl, BikeControl, TruckControl
# Demonstrate calling each through a single interface.

class VehicleControl(ABC):
    @abstractmethod
    def brake(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def steer(self):
        print("brake")
class Bike(VehicleControl):
    def accelerate(self):
        print("accelerate")
    def brake(self):
        print("brake")
class GT650(Bike):
    def steer(self):
        print("steer")
obj=GT650()
obj.brake()
obj.steer()


#  Using abc module:
# • Create an abstract class Shape with
# area(), perimeter()
# • Implement Circle, Rectangle, Triangle
# Demonstrate:
# • why base class should NOT contain calculation logic
# • what happens if a subclass fails to implement
# one of the methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("area")
    @abstractmethod
    def perimeter(self):
        print("perimeter")
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        super().area()
        print(3.14*self.radius*self.radius)
    def perimeter(self):
        print(2*3.14*self.radius)
c1=Circle(3)
c1.area()
c1.perimeter()
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPIPayment(Payment):
    def pay(self):
        print("UPI payment logic")