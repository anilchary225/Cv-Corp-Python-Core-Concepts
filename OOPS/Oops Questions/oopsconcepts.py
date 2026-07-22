import math
from abc import ABC,abstractmethod

'''
You are building a notification system for a large-scale application such as a
banking platform or an online learning portal.
The system must support sending notifications through multiple channels such
as email, SMS, and push notifications.
Design a class named Notifier that represents the idea of sending a notification, not the
actual implementation.
This class must:
• Contain a method named send(message) whose responsibility is to send a message
to a user.
• Not provide any implementation for send(), because the way an email is sent is
fundamentally different from how an SMS or push notification is sent.
• Force every class that represents a specific notification type to provide its own
implementation of send().
Now create three separate classes:
• EmailNotifier
• SMSNotifier
• PushNotifier
Each of these classes must:
• Provide its own logic for sending the message.
• Store sensitive configuration details (such as API keys or server settings) in such a
way that they cannot be modified directly from outside the class.
Write client code that:
• Accepts a list of notifier objects.
• Calls send() on each object without checking what type of notifier it is.
Finally, explain within your answer:
• Why the base Notifier class should not contain any actual sending logic.
• Why forcing child classes to implement send() is safer than trusting developers to
remember it.
• Why writing if/else conditions based on notification type would become a problem
as the system grows.
'''

# class Notifier(ABC):
#     @abstractmethod
#     def send(self,message):
#         pass
# class EmailNotifier(Notifier):
#     def __init__(self):
#         self.__smtp_server='smtp.gmail.com'
#         self.__api_key='shjbdjhvbsjdhb'
#
#     def send(self,message):
#         print(f'sending Email: {message}')
# class SMSNotifier(Notifier):
#     def __init__(self):
#         self.__sms_gateway='messenger'
#         self.__api_key='bsdfhbs'
#
#     def send(self,message):
#         print(f'sending message: {message}')
#
# class PushNotifier(Notifier):
#     def __init__(self):
#         self.__firebase_key='dsbvjd'
#
#     def send(self,message):
#         print(f'sending push notification :{message}')
#
# notifiers = {
#     EmailNotifier(),
#     SMSNotifier(),
#     PushNotifier()
# }
#
# # for notifier in notifiers:
# #     notifier.send('Your payment is done')
#
# for notify in notifiers:
#     if isinstance(notify,EmailNotifier):
#         notify.send('Your payment is done through Email')
#     elif isinstance(notify,SMSNotifier):
#         notify.send('Your Payment id done through SMS')
#     elif isinstance(notify,PushNotifier):
#         notify.send('Your payment is done through PUSH_NOTIFICATION')
#     else:
#         print('Invalid Notifier')


'''
2. You are developing a payment processing module for an e-commerce website.
The system supports multiple payment methods, and each payment method follows a
different processing flow.
Create a class named PaymentProcessor that represents the general concept of processing
a payment.
This class must:
• Define a method called process_payment(amount) which represents the act of
charging a user.
• Not assume how the payment is processed, because card payments, UPI payments,
and wallet payments all work differently.
• Contain a helper method used internally for validation, which should not be accessed
directly from outside the class.
Create specialized classes for:
• Credit card payments
• UPI payments
• Wallet payments
Each specialized class must:
• Provide its own version of process_payment().
• Reuse shared validation behavior without duplicating code.
Write client code that:
• Takes a payment object and processes payment without knowing which payment
method is being used.
Explain:
• Why keeping all payment logic in a single function leads to fragile code.
• Why allowing subclasses to redefine behavior makes the system easier to extend.
• Why internal validation methods should not be publicly accessible.
'''



# Abstract Base Class
# class PaymentProcessor(ABC):
#
#     # Internal validation method
#     def __validate(self, amount):
#         if amount <= 0:
#             return False
#         return True
#
#     # Shared validation access for subclasses
#     def _validate_payment(self, amount):
#         return self.__validate(amount)
#
#     @abstractmethod
#     def process_payment(self, amount):
#         pass
#
#
# # Credit Card Payment
# class CreditCardPayment(PaymentProcessor):
#
#     def process_payment(self, amount):
#
#         if self._validate_payment(amount):
#             print(f"Processing Credit Card Payment of ₹{amount}")
#         else:
#             print("Invalid Amount")
#
#
# # UPI Payment
# class UPIPayment(PaymentProcessor):
#
#     def process_payment(self, amount):
#
#         if self._validate_payment(amount):
#             print(f"Processing UPI Payment of ₹{amount}")
#         else:
#             print("Invalid Amount")
#
#
# # Wallet Payment
# class WalletPayment(PaymentProcessor):
#
#     def process_payment(self, amount):
#
#         if self._validate_payment(amount):
#             print(f"Processing Wallet Payment of ₹{amount}")
#         else:
#             print("Invalid Amount")
#
#
# # Client Code
# def make_payment(payment_method, amount):
#     payment_method.process_payment(amount)
#
#
# # Objects
# credit = CreditCardPayment()
# upi = UPIPayment()
# wallet = WalletPayment()
#
# # Processing Payments
# make_payment(credit, 5000)
# make_payment(upi, 1200)
# make_payment(wallet, 300)

'''
Create a class Employee that stores:
• An employee’s name (should be freely accessible).
• The department they work in (should be accessible only to subclasses).
• The employee’s salary (should never be directly accessed or modified from outside
the class).
Ensure that:
• The salary value cannot be accidentally overridden or accessed using its original
name.
• Any attempt to access salary directly from outside clearly demonstrates how Python
internally alters such names.
Create a subclass Manager that:
• Introduces its own salary-related logic.
• Demonstrates what happens when a subclass defines an attribute with the same name
as one in the parent class.
'''



# class Employee(ABC):
#     def __init__(self,en,d,salary):
#         self.e_name=en
#         self._dpt=d
#         self.__salary=salary
#
#     def show_salary(self):
#         print(self.__salary)
# class Manager(Employee):
#     def __init__(self,name,department,salary,bonus):
#         super().__init__(name,department,salary)
#         self.__salary=bonus
#
#     def manager_salary(self):
#         print('Manager salary: ',self.__salary)
#     def show_department(self):
#         print('department: ',self._dpt)
#
# emp=Employee('Anil','IT',29999)
# print(emp.e_name)
# print(emp._dpt)
# emp.show_salary()
#
# print(emp.__dict__)
#
# mgr=Manager('Abdul','CSE',200000,80000)
# mgr.manager_salary()
# mgr.show_salary()
# mgr.show_department()




'''
You are tasked with designing a logging system for an enterprise application.
The system must support writing logs to:
• Files
• Databases
• External monitoring systems
Instead of creating a deep inheritance hierarchy, design the system such that:
• A Logger object does not directly know how logs are written.
• The responsibility of writing logs is delegated to another object.
Create separate writer classes, each responsible for a specific destination.
Your design must allow:
• Switching the logging destination at runtime.
• Adding new log destinations without modifying existing code.
Explain:
• Why inheriting one logger from another would tightly couple the system.
• Why delegating responsibilities produces a more flexible design.
• Why this approach is easier to test and maintain.

'''


# Writer Interface
# class LogWriter(ABC):
#
#     @abstractmethod
#     def write(self, message):
#         pass
#
#
# # File Logger
# class FileWriter(LogWriter):
#
#     def write(self, message):
#         print(f"Writing log to FILE: {message}")
#
#
# # Database Logger
# class DatabaseWriter(LogWriter):
#
#     def write(self, message):
#         print(f"Writing log to DATABASE: {message}")
#
#
# # External Monitoring Logger
# class MonitoringWriter(LogWriter):
#
#     def write(self, message):
#         print(f"Sending log to MONITORING SYSTEM: {message}")
#
#
# # Logger Class
# class Logger:
#
#     def __init__(self, writer):
#         self.writer = writer
#
#     def set_writer(self, writer):
#         self.writer = writer
#
#     def log(self, message):
#         self.writer.write(message)
#
#
# # Client Code
#
# # File Logging
# file_logger = FileWriter()
# logger = Logger(file_logger)
#
# logger.log("Application Started")
#
#
# # Switching to Database Logging at Runtime
# db_logger = DatabaseWriter()
# logger.set_writer(db_logger)
#
# logger.log("User Login Success")
#
#
# # Switching to Monitoring System
# monitor_logger = MonitoringWriter()
# logger.set_writer(monitor_logger)
#
# logger.log("Server CPU Usage High")


'''
You are creating a system that calculates the area of different geometric shapes.
Design a base class that represents the concept of a shape.
This class must:
• Define a method named area().
• Not provide any formula, because the formula depends entirely on the shape type.
• Prevent the creation of objects that do not define how area is calculated.
Create concrete shape classes such as rectangle, circle, and triangle.
Write code that:
• Stores different shapes in a single collection.
• Calculates area without checking which shape it is.
Explain:
• Why forcing every shape to implement area() avoids runtime errors.
• Why using condition-based logic is harder to scale.
• Why this design makes future shapes easy to add.
'''


# class Calculate_area(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Calculate_area):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#
#
#     def area(self):
#         print('area of rectangle: ',self.length*self.width)
#
# class Circle(Calculate_area):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print('Circle Area: ',math.pi*self.radius*self.radius)
#
# class Traingle(Calculate_area):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         print('Triangle area: ',0.5*self.base*self.height)
# shapes=[
#     Rectangle(10,20),
#     Circle(5),
#     Traingle(12,15)
# ]
#
# for shape in shapes:
#     if isinstance(shape,Rectangle):
#         shape.area()
#     elif isinstance(shape,Circle):
#         shape.area()
#     elif isinstance(shape,Traingle):
#         shape.area()



'''
You are designing an order pricing system.
An order’s final price depends on:
• Base price
• Discounts
• Taxes
Design separate classes that:
• Each handle exactly one responsibility.
• Can be combined together to compute the final price.
Create a final order class that:
• Inherits behavior from multiple pricing-related classes.
• Clearly demonstrates how Python decides which method to execute when multiple
classes define the same method.
Explain:
• How Python determines execution order.
• Why careless multiple inheritance can introduce bugs.
• Why this pattern should be used sparingly.

'''
#
# class Order_Praising_system(ABC):
#     @abstractmethod
#     def base_price(self):
#         pass
#     @abstractmethod
#     def discounts(self,dp):
#         pass
#     @abstractmethod
#     def taxes(self,tp):
#         pass
#
# class Order(Order_Praising_system):
#     def __init__(self,bp):
#         self.base_price_amount=bp
#
#     def base_price(self):
#         print('Base price: ',self.base_price_amount)
#     def discounts(self,discount_percentage):
#         self.discount=self.base_price_amount*(discount_percentage/100)
#         self.final_amount=self.base_price_amount+self.discount
#         print('Discount on order: ',self.discount)
#
#     def taxes(self,tax_percentage):
#         self.tax_price=self.base_price_amount*(tax_percentage/100)
#         self.final_amount+=self.tax_price
#         print('Tax on order: ',self.tax_price)
#
#     def final_price(self):
#         print('final amount on order: ',self.final_amount)
#
# ord=Order(1000)
# ord.base_price()
# ord.discounts(10)
# ord.taxes(10)
# ord.final_price()


'''
You are building a plugin system for a software platform.
A plugin is considered valid if it:
• Provides a method named run().
Do not enforce inheritance from a base class.
Write code that:
• Accepts any object as a plugin.
• Executes run() without checking the object’s type or class hierarchy.
Explain:
• Why this approach makes the system more flexible.
• Why checking behavior is better than checking type.
• Why this pattern fits Python better than rigid class hierarchies.
'''

# class AudioPlugins:
#     def run(self):
#         print('Audio Plugins')
# class MediaPlugin:
#     def run(self):
#         print('Media Plugin')
# class APIPlugin:
#     def run(self):
#         print('API Plugin')
#
# ap=AudioPlugins()
# mp=MediaPlugin()
# api=APIPlugin()
#
# plugins=[ap,mp,ap]
#
# for plugin in plugins:
#     # print(plugin)
#     if isinstance(plugin,AudioPlugins):
#         plugin.run()
#     elif isinstance(plugin,MediaPlugin):
#         plugin.run()
#     elif isinstance(plugin,APIPlugin):
#         plugin.run()
#     else:
#         print('Invalid Plugin')

'''
Design a BankAccount class.
The balance:
• Must not be directly modified.
• Must always be validated before updating.
Expose balance access in a way that:
• Looks like normal attribute access.
• Internally executes validation logic.
Explain:
• Why direct attribute access can corrupt system state.
• Why controlled access is essential in financial systems.
• Why this approach is more Pythonic than traditional getter/setter methods.
'''

# class BankAccount:
#
#     def __init__(self, balance):
#
#         # Private Attribute
#         self.__balance = 0
#
#         # Using setter validation
#         self.balance = balance
#
#     # Getter
#     @property
#     def balance(self):
#         return self.__balance
#
#     # Setter
#     @balance.setter
#     def balance(self, amount):
#
#         if amount < 0:
#             print("Invalid Balance Amount")
#
#         else:
#             self.__balance = amount
#
#
# # Object Creation
# acc = BankAccount(5000)
#
# # Looks like normal attribute access
# print(acc.balance)
#
# # Updating balance
# acc.balance = 8000
# print(acc.balance)
#
# # Invalid update
# acc.balance = -2000
#
# print(acc.balance)



from abc import ABC, abstractmethod


# Base Vehicle Class
class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass


# Engine Capability
class EngineVehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


# Petrol Car
class Car(Vehicle, EngineVehicle):

    def move(self):
        print("Car is moving")

    def start_engine(self):
        print("Car engine started")


# Bike
class Bike(Vehicle, EngineVehicle):

    def move(self):
        print("Bike is moving")

    def start_engine(self):
        print("Bike engine started")


# Electric Scooter
class ElectricScooter(Vehicle):

    def move(self):
        print("Electric Scooter is moving")



'''
You are designing a vehicle system.
Initially, all vehicles are assumed to have engines.
Later, electric vehicles are introduced.
Design a system where:
• Subclasses can replace base classes without breaking functionality.
• No subclass is forced to implement meaningless behavior.
Explain:
• What goes wrong when assumptions are baked into base classes.
• How redesigning abstractions fixes the issue.
• Why poor base class design causes long-term damage.
'''


# Client Code
# vehicles = [
#     Car(),
#     Bike(),
#     ElectricScooter()
# ]
#
# for vehicle in vehicles:
#     vehicle.move()
#
#
# # Engine-specific operations
# engine_vehicles = [
#     Car(),
#     Bike()
# ]
#
# for vehicle in engine_vehicles:
#     vehicle.start_engine()


'''
Design an authentication system for a SaaS application.
The system must:
• Support multiple authentication mechanisms.
• Protect sensitive credentials.
• Allow future authentication methods without modifying existing logic.
Your design should naturally demonstrate:
• Separation of responsibility
• Controlled data access
• Flexible behavior extension
• Safe reuse of logic
Explain:
• Why a single procedural authentication function is dangerous.
• Why this design is scalable and secure.
• Why real-world systems rely on these principles.
'''


# # Abstract Authentication Class
# class Authentication(ABC):
#
#     def __init__(self, username, password):
#
#         # Protected Attribute
#         self._username = username
#
#         # Private Attribute
#         self.__password = password
#
#     # Shared Validation Logic
#     def _validate_credentials(self):
#
#         if len(self.__password) >= 6:
#             return True
#
#         return False
#
#     @abstractmethod
#     def authenticate(self):
#         pass
#
#
# # Email Authentication
# class EmailAuth(Authentication):
#
#     def authenticate(self):
#
#         if self._validate_credentials():
#             print(f"Email Authentication Successful for {self._username}")
#         else:
#             print("Invalid Email Credentials")
#
#
# # Google OAuth Authentication
# class GoogleAuth(Authentication):
#
#     def authenticate(self):
#
#         if self._validate_credentials():
#             print(f"Google Authentication Successful for {self._username}")
#         else:
#             print("Invalid Google Credentials")
#
#
# # OTP Authentication
# class OTPAuth(Authentication):
#
#     def authenticate(self):
#
#         if self._validate_credentials():
#             print(f"OTP Authentication Successful for {self._username}")
#         else:
#             print("Invalid OTP Credentials")
#
#
# # Client Code
# def login(auth_method):
#     auth_method.authenticate()
#
#
# # Objects
# email_user = EmailAuth("anil@gmail.com", "pass123")
# google_user = GoogleAuth("anil@gmail.com", "google789")
# otp_user = OTPAuth("9876543210", "otp456")
#
#
# # Authentication
# methods = [email_user, google_user, otp_user]
#
# for method in methods:
#     login(method)