'''
Singleton class
'''
#
# class A:
#     x=None
#     def __new__(cls):
#         if cls.x is None:
#             cls.x=super().__new__(cls)
#         return cls.x
# obj=A()
# print(obj)
# obj1=A()
# print(obj1)


# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#
#     def display_student(self):
#         print('name ',self.name,'age ', self.age)
#     def grade_student(self):
#         if self.marks>=90:
#             self.grade='A'
#         elif self.marks>=80:
#             self.grade='B'
#         elif self.marks>=70:
#             self.grade='C'
#         elif self.marks>=60:
#             self.grade='D'
#         else:
#             self.grade='F'
#     def validate(self):
#         return self.marks>=40
#
# obj=student('anil',23,87)
# obj.display_student()
# obj.grade_student()
# print(obj.grade)
# print(obj.validate())


'''
Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed.
'''

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def is_passed(self):
#         if self.marks>40:
#             return 'Pass'
#         else:
#             return 'Fail'
#
# obj=Student('Anil',80)
# obj1=Student('Abdul',30)
# print(obj.name,obj.marks,obj.is_passed())
# print(obj1.name,obj1.marks,obj1.is_passed())

'''
# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a method change_company(self, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
'''


# class Employee:
#     company_name='TechCorp'
#
#     def __init__(self,name):
#         self.name=name
#     def change_company(self,new_name):
#         Employee.company_name= new_name
#     def display(self):
#         print(f'name:{self.name}, Company_name: {Employee.company_name}')
#
# e1=Employee('Anil')
# e2=Employee('Abdul')
#
# print('Before')
#
# e1.display()
# e2.display()
#
# e1.change_company('Google')
#
# print('After change')
# e1.display()
# e2.display()


"""# Q3. Create a class MathOps with a method is_even(num) that returns True if the number is even.
# Then call it both from the an instance."""

# class MathOps:
#     def is_even(self,num):
#         if num%2==0:
#             return True
#         else:
#             return False
#
# print(MathOps().is_even(2))

'''
Q4. Create a class Car with:
• instance attribute mileage
• class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.
'''
# class car:
#     wheels= 4
#     def __init__(self,m):
#         self.mileage=m
#
#     def display_specs(self):
#         print('mileage: ',self.mileage,'Wheels: ',self.wheels)
#
# Hyundai=car(17)
# Hyundai.display_specs()
#

'''
Q5. Create a class Temperature with:
instance attribute celsius
a static method to_fahrenheit(celsius)
an instance method show_conversion() that uses the static method to print both values.
'''

# class ctof:
#
#
#     @staticmethod
#     def to_fahrenheit(c):
#         print((9/5)*c+32)
#
#
# ctof.to_fahrenheit(50)


'''
Q7. Create a class Employee with:
instance attributes: name, base_salary
class variable: bonus_rate = 0.1
instance method: final_salary() → base_salary + (base_salary × bonus_rate)
class method: update_bonus(cls, new_rate) → updates bonus for all employees
static method: is_valid_salary(sal) → checks if salary > 0
Create two employees, show final salaries, update bonus rate, and show again.
'''



# class Employee:
#     bonus_rate=0.1
#     def __init__(self,name,base_salary):
#         self.name=name
#         self.base_salary=base_salary
#
#     def final_salary(self):
#         print(self.base_salary+(self.base_salary*Employee.bonus_rate))
#
#     @classmethod
#     def update_bonus(cls,new_rate):
#         cls.bonus_rate=new_rate
#
#     @staticmethod
#     def is_valid(sal):
#         return sal>0
#
# e1=Employee('Anil',30000)
# e1.final_salary()
# print(e1.bonus_rate)
# print(Employee.bonus_rate)
# print(e1.name,e1.base_salary,e1.is_valid(30000))
# e1.update_bonus(2)
# e1.final_salary()
# print(e1.is_valid(0))




'''
Q8. Create a class Course with:
class variable total_students
instance variable student_name
instance method enroll() → increments total_students
class method show_total(cls) → prints total students
static method is_eligible(age) → returns True if age ≥ 18
Demonstrate enrolling multiple students and show total count.

'''

# class Course:
#     total_students=100
#     def __init__(self,n):
#         self.name=n
#
#     def enroll(self):
#         Course.total_students+=1
#
#     @classmethod
#     def show_total(cls):
#         print(cls.total_students)
#
#     @staticmethod
#     def is_eligible(age):
#         return age>=18
# s1=Course("Anil")
# s1.enroll()
# s1.show_total()
# print(s1.is_eligible(18))
# s2=Course('Abdul')
# s2.enroll()
# print(s2.name)
# s2.show_total()



'''
Q9. Create a class BankAccount with:
class variable bank_name
instance variables holder and balance
instance method deposit(amount)
class method change_bank_name(cls, new_name)
static method validate_amount(amount) → returns True if amount > 0
Show transactions and how static + class methods work together.

'''

# class BankAccount:
#     bank_name='sbi'
#     def __init__(self,h,b):
#         self.holder=h
#         self.balance=b
#
#     def deposit(self,amount):
#         self.balance+=amount
#     @classmethod
#     def change_bank_name(cls,new_bank):
#         cls.bank_name=new_bank
#
#     @staticmethod
#     def validate_amount(amount):
#         return amount>0
#
# b1=BankAccount('Anil',200000)
# print(b1.holder,b1.balance)
# b1.deposit(50000)
# print(b1.balance)
# print(b1.bank_name)
# b1.change_bank_name('bob')
# print(b1.bank_name)
# print(b1.validate_amount(10000))


'''
Q10. Create a class Student with:
class variable passing_marks = 40
instance attributes name, marks
instance method result() → prints pass/fail using class variable
class method update_passing_marks(cls, new_marks)
static method grade_category(marks) → returns "A", "B", "C" based on score ranges
Use all three in a program that:
Creates students
Updates the passing criteria
Displays grade category and result
'''

# class Student:
#     passing_marks=40
#     def __init__(self,n,m):
#         self.name=n
#         self.marks=m
#
#     def result(self):
#         return self.marks>Student.passing_marks
#
#     @classmethod
#     def update_passing_marks(cls,pass_marks):
#         cls.passing_marks=pass_marks
#
#     @staticmethod
#     def grade_category(marks):
#         if marks>90:
#             return 'A'
#         elif marks>80:
#             return 'B'
#         elif marks>70:
#             return 'C'
#         elif marks>80:
#             return 'D'
#         else:
#             return 'E'
# stu1=Student('Anil',45)
# print(stu1.passing_marks)
# print(stu1.grade_category(89))
# print(stu1.result())
# stu1.update_passing_marks(50)
# print(stu1.passing_marks)



'''
Q6. Create a class Book with:
instance attributes title, author
a class variable total_books
a class method from_string(cls, book_str) that creates an object from "title-author" format
a static method is_valid_title(title) that checks if title has at least 3 characters
increment total_books for every book created
Demonstrate:
Creating books using both the constructor and the class method
Validating titles before creation

'''

#
# class Book:
#     total_books=10
#
#     def __init__(self,t,a):
#         self.title=t
#         self.author=a
#         Book.total_books+=1
#
#     @classmethod
#     def from_str(cls,s):
#         title,author=s.split('-')
#         return cls(title,author)
#
#     @staticmethod
#     def is_valid(t):
#         return len(t)>3
# obj=Book.from_str('NSNS-Koushik')
# print(obj.title)
# print(obj.author)
# print(obj.total_books)
# print(Book.is_valid(obj.title))
#
# obj=Book.from_str('bhahubali-rajamouli')
# print(obj.title)
# print(obj.author)
# print(obj.total_books)
# print(Book.is_valid(obj.title))
#
# obj=Book.from_str('RRR-rajamouli')
# print(obj.title)
# print(obj.author)
# print(obj.total_books)
# print(obj.is_valid(obj.title))

'''
Q2. Design a class Product that:
Maintains a base tax rate applicable to all products.
Each product has a name and base price.
Has a method to compute final price including tax.
Can change tax rate for all products using one method.
Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
Creating multiple products.
Changing the tax rate.
Showing updated prices and validity checks.
'''


# class Product:
#     base_tax_price=10
#     def __init__(self,n,p):
#         self.name=n
#         self.price=p
#
#     def final_price(self):
#         return self.price+self.base_tax_price
#
#     @classmethod
#     def change_tax_price(cls,new_tax):
#         cls.base_tax_price=new_tax
#
#     @staticmethod
#     def valid(p):
#         return p>=0
#
#     def display(self):
#         p1 = Product('Anil', 6000)
#         finalprice = p1.final_price()
#         valid = p1.valid(p1.price)
#         print('name: ', p1.name, 'price: ', p1.price, ' final price: ', finalprice, 'price valid : ', valid)
#
# p1=Product('Anil',6000)
# p1.display()
# p1.change_tax_price(20)
# p1.display()
# p1.change_tax_price(200)
# p1.display()

# final_price=p1.final_price()
# valid = p1.valid(p1.price)
# print('name: ',p1.name, 'price: ',p1.price, ' final price: ',final_price, 'price valid : ',valid )
# p1.change_tax_price(20)
# final_price=p1.final_price()
# valid = p1.valid(p1.price)
# print('name: ',p1.name, 'price: ',p1.price, ' final price: ',final_price, 'price valid : ',valid )



'''
Q3. Create an Employee class that:
Keeps a minimum experience required for promotion (shared across all employees).
Stores employee name, experience, and department.
Has a method to check eligibility for promotion.
Provides a function to update promotion criteria globally.
Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
Creating employees from different departments.
Changing promotion criteria.
Displaying eligibility results and department validation.

'''


# class Employee:
#     min_exp=2
#
#     def __init__(self,em,e,d):
#         self.employee_name=em
#         self.experience=e
#         self.department=d
#     def eligibility(self):
#         return self.experience>self.min_exp
#     @classmethod
#     def update_min_exp(cls,me):
#         cls.min_exp=me
#
#     @staticmethod
#     def valid_dep(dn):
#         l=['Admin','Tech','Hr']
#         for i in l:
#             return True if dn==i else False
#         return None
#     def display(self):
#         valid=self.valid_dep(self.department)
#         eligible=self.eligibility()
#         print('Employee name: ',self.employee_name , "\nExperience: ",self.experience, '\nDepartment: ',self.department, '\nis valid department: ',valid, '\nis employee eligible: ',eligible)
#
# e1=Employee('Charan',5,'Admin')
# e1.display()
# e1.update_min_exp(8)
# e1.display()
# e2=Employee('Charan',5,'AIML')
# e2.display()

'''
Q4. Build a Loan class that:
Has a common interest rate for all loans.
Each object stores borrower name and principal.
Calculates total payable amount.
Provides a function to update the interest rate.
Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
Creating multiple loan accounts.
Updating interest rates.
Checking eligibility and total repayment for borrowers.

'''


# class Loan:
#     interest_rate=3
#     threshold=100
#     def __init__(self,bn,p):
#         self.borrower_name=bn
#         self.principle=p
#
#     def total_payable_amount(self):
#         return self.principle+self.principle*(self.interest_rate/100)
#
#     @classmethod
#     def change_tax(cls,new_tax):
#         cls.interest_rate=new_tax
#
#     @staticmethod
#     def is_valid(s,t):
#         return s>t
#
#     def display(self):
#
#         total=self.total_payable_amount()
#         print('name: ',self.borrower_name, 'Principle: ',self.principle, 'Total: ',total, self.is_valid(total,self.threshold))
# l1=Loan('Anil',40000)
# l1.display()


'''
Q5. Create a class Course that:
Tracks total courses created.
Each course has a title, duration, and enrolled_students.
Provides a method to enroll a new student.
Allows updating the minimum duration for a valid course across all instances.
Has a static function to check if a given duration is realistic (not negative, not too large).
Demonstrate:
Creating multiple courses.
Enrolling students.
Updating minimum duration and checking durations.

'''


# class Course:
#     total_courses=0
#     def __init__(self,t,d,es):
#         self.title=t
#         self.duration=d
#         self.enrolled_students=es
#         Course.total_courses+=1
#
#     def enroll_new_student(self,new_student):
#         self.enrolled_students=new_student
#
#     def update_duration(self,new_d):
#         self.duration=new_d
#
#     @staticmethod
#     def valid_duration(d):
#         return d>0
#
#     def display(self):
#         valid=self.valid_duration(self.duration)
#         print('Title: ',self.title,'\nDuration: ',self.duration, '\nEnrolled students: ',self.enrolled_students,'\nValid Duration: ',valid,'\nTotal Courses: ',self.total_courses)
#
# c1=Course('AI',4,12)
# c1.display()
# print()
# c1.enroll_new_student(15)
# c1.update_duration(10)
# c1.display()
# print()
# c1=Course('ML',6,15)
# c1.display()
# print()
# c1=Course('CSE',9,30)
# c1.display()



# n=list(map(int,input.split()))

'''
Q6. Design a class Vehicle that:
Keeps a record of service charge rate common to all vehicles.
Each vehicle has a model, kilometers_run, and service history.
Has a function to calculate service charge based on km and rate.
Provides a method to update the service rate for all vehicles.
Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
Demonstrate:
Creating vehicles with different km and models.
Updating the service rate.
Showing charges and eligibility checks.

'''


# class Vehicle:
#     service_charge_rate=120
#     def __init__(self,model,km_r,service_h):
#         self.model=model
#         self.kilometer_runs=km_r
#         self.service_history=service_h
#
#     def calculate_service_charge(self):
#         c=0
#         while self.kilometer_runs > c:
#             c+=1000
#         return self.service_charge_rate+(c-1000) // 100
#
#     @classmethod
#     def update_service_charge(cls,new_service_charge):
#         cls.service_charge_rate=new_service_charge
#
#     @staticmethod
#     def eligible_model(m):
#         from  datetime import date
#         current_year=date.today().year
#         return False if current_year-m<15 else True

#     def display(self):
#         service_charge=self.calculate_service_charge()
#         eligible=self.eligible_model(self.model)
#         print('Model: ',self.model, '\nKilometer runs: ',self.kilometer_runs, '\nService_history: ',self.service_history,'\nVehicle Service charge based on kilometers runs: ',service_charge, '\nEligible: ',eligible)
#
# v1=Vehicle(2015,200000,7)
# v1.display()
# v1.eligible_model(2019)  # we can also send only model number instead of object creation


'''

Q7. Build an Inventory class that:
Tracks the total number of items across all inventories.
Each instance maintains its own stock dictionary ({"item": quantity}).
Provides a method to add or remove stock.
Allows updating a minimum stock threshold globally.
Offers a static checker to verify if a stock level is below threshold.
Demonstrate:
Managing multiple inventories.
Adjusting stock threshold.
Using static validation inside the instance logic.

'''

# class Inventory:
#     total_items=0
#     threshold=3
#     def __init__(self):
#         self.items={}
#
#     def add(self,i,q):
#         self.items[i]=q
#         Inventory.total_items+=1
#
#     def sub(self,i):
#         self.items.remove(i)
#         Inventory.total_items-=1
#     @classmethod
#     def change_threshold(cls,nt):
#         cls.threshold=nt
#
#     @staticmethod
#     def valid(q,t):
#         return q<t
#     def display(self,i):
#         print('item: ',i)
#
# i1=Inventory()
# i1.add('oats',5)
# i2=Inventory()
# i2.add('protein',50)
# i1.display(i1.items['oats'])
# i2.display(i2.items['protein'])

'''
Q8. Create a HotelRoom class that:
Keeps a base price per night (shared).
Each room has room_number, nights_booked, and guest_name.
Has a method to calculate total bill.
Allows updating the base price across all rooms.
Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
Demonstrate:
Creating rooms and bookings.
Changing base price.
Checking bill updates and validation.
'''

# class Hotel_Room:
#     base_price=500
#     def __init__(self,rn,nb,gn):
#         self.room_number=rn
#         self.nights_booked=nb
#         self.guest_name=gn
#
#     def bill(self):
#         return self.nights_booked*self.base_price
#     @classmethod
#     def update_base_price(cls,new_price):
#         cls.base_price=new_price
#
#     @staticmethod
#     def valid(nd):
#         return nd>2
#
#     def display(self):
#         print('Room No: ',self.room_number, '\nGuest Name: ',self.guest_name, '\nNo of Nights Booked: ',self.nights_booked,'\nValid: ',self.valid(self.nights_booked))
#
# h1=Hotel_Room(3,8,'Abdul')
# h1.display()
# h1.update_base_price(1000)
# print()
# h2=Hotel_Room(5,1,'nazaria')
# h2.display()


'''

Q9. Design a LibraryMember class that:
Tracks total active members.
Each member has a name and books_borrowed count.
Has a function to borrow books, with borrowing limit common to all.
Allows updating borrowing limit globally.
Has a static function to check if book title is valid (non-empty string, reasonable length).
Demonstrate:
Borrowing books for multiple users.
Changing borrowing limits.
Validating book titles before borrowing.

'''

# class LibraryMember:
#     total_active_members=10
#     limit=3
#     def __init__(self,n,bb):
#         self.name=n
#         self.books_borrowed=bb
#         LibraryMember.total_active_members+=1
#
#     def books_borrowing(self):
#         return self.books_borrowed<=self.limit
#     @classmethod
#     def update_borrow_books(cls,new_limit):
#         cls.limit=new_limit
#
#     @staticmethod
#     def valid_title(t):
#         return len(t)>0
#
#     def display(self):
#         print('Name: ',self.name,'\nBooks Borrowed: ',self.books_borrowed, '\nTotal Active members: ',self.total_active_members,"\nis books borrows is in limited: ",self.books_borrowing())
#
# l1=LibraryMember('Anil',4)
# l1.display()
# print()
# l1.update_borrow_books(5)
# l1.display()

'''
Q10. Create a class Member that:
Has a shared BMI limit for “fit” status.
Each member stores name, height, weight.
Has a method to calculate BMI and check fit status.
Provides a function to update BMI limit for all members.
Offers a tool to check if height and weight entered are valid numbers.
Demonstrate:
Creating multiple members.
Updating BMI standard.
Displaying fit status and input validity.

'''


# class Member:
#     BMI_Limit=18
#     def __init__(self,n,h,w):
#         self.name=n
#         self.height=h
#         self.weight=w
#
#     def calculate_bmi(self):
#         bmi=self.weight//(self.height**2)  #height in meters and weight in kgs
#         # print(bmi)
#         return 'Fit' if bmi<self.BMI_Limit else 'UnFit'
#     @classmethod
#     def update_bmi_limit(cls,new_bmi_limit):
#         cls.BMI_Limit=new_bmi_limit
#
#     @staticmethod
#     def valid_height_weight(h,w):
#         return h>0 and w>0
#
#     def display(self):
#         if self.valid_height_weight(self.height,self.weight):
#             print('Name: ',self.name, '\nHeight: ',self.height, '\nWeight: ',self.weight, '\nBMI Calculation: ',self.calculate_bmi())
#         else:
#             print('Given height Weight are negative or in different formats')
# m1=Member('Anil',66,65)
# m1.display()
# m1.update_bmi_limit(25)
# print()
# m1.display()

''' Singleton Class'''


# class singleton_A:
#     x=None
#     def __new__(cls):
#         if cls.x is None:
#             cls.x=super().__new__(cls)
#         return cls.x
# obj1=singleton_A()
# print(obj1)
# obj2=singleton_A()
# print(obj2)



'''
Create a class TimeTraveler with:
•instance attributes codename, origin_year, destination_year
•a class variable registry that stores all created traveler objects
•a class method show_registry() → displays total number of travelers and prints their codenames
•a static method year_status(year) → returns "Past", "Present", or "Future" based on the current year

Use all three in a program that:
1.Creates multiple time traveler objects
2.Displays the registry details using the class method
3.Checks different years using the static method and prints their status
'''
# class TimeTraveler:
#     total_travelers=0
#     def __init__(self,cn,oy,dy):
#         self.codename=cn
#         self.origin_year=oy
#         self.destination_year=dy
#         TimeTraveler.total_travelers+=1
#
#     @classmethod
#     def show_registry(cls):
#         return cls.total_travelers
#
#     @staticmethod
#     def year_status(yr):
#         from datetime import date
#         current_year = date.today().year
#         if yr < current_year:
#             return 'Past'
#         elif yr == current_year:
#             return 'Present'
#         else:
#             return 'Future'
#
#     def display(self):
#         print('Codename: ',self.codename,'\norigin year: ',self.origin_year,'\ndestination: ',self.destination_year,'\nTotal Number of Registers: ',self.show_registry(),'\nYear Status: ',self.year_status(self.origin_year))
#
# t1=TimeTraveler('EV',2023,2030)
# t1.display()

