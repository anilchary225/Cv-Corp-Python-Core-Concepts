'''1 question

1) Add Before & After Messages
Create a decorator that prints "Start" before the function execution and "End" after it finishes.
• Expected Output:
o Start
o Hello
o End
'''
# def hello(f):
#     def wrapper(*args,**kwargs):
#         print('Start')
#         f()
#         print('End')
#     return wrapper
#
# @hello
# def fun():
#     print('Hello World')
#
# fun()

'''2nd question
2) Decorator With Input (Parameters)
Create a decorator that works for a function taking a name as input. It should print "Starting..."
before greeting the user.
• Function: def greet(name): print("Hello", name)
• Expected Output:
o Starting...
o Hello Ravi
o Done
'''

# def greeting(g):
#     def wrapper(*args,**kwargs):
#         print('Starting')
#         g(*args,**kwargs)
#         print('End')
#     return wrapper
# @greeting
# def greet(n):
#     print('Hello, ',n)
# greet('Anil')

'''3rd question
3) Result Doubler
Create a decorator that captures the value returned by a function and multiplies it by 2 before
returning it.
• Example: If the function returns 25, the final output should be 50.
'''

# def multiply(m):
#     def wrapper(*args,**kwargs):
#         m(*args,**kwargs)
#     return wrapper
# @multiply
# def mul(x):
#     print(x*2)
# mul(25)

'''4th question
4) Admin Access Check
Create a decorator that checks a user_role variable. If the role is not "admin", it should print
"Access Denied" and prevent the function from running.
• Expected Output: Access Denied (if user is a 'student').
5) Uppercase Output
Create a decorator that takes a string returned by a function and converts the entire string to
uppercase.
• Function: def get_msg(): return "hello world"
• Expected Output: HELLO WORLD
'''


# def check(c):
#     def wrapper(*args,**kwargs):
#         if c()=='Admin':
#             return 'Access'
#         return 'Access Denied'
#     return wrapper
# @check
# def c():
#     return 'Admin'
# print(c())

'''5th question
5) Uppercase Output
Create a decorator that takes a string returned by a function and converts the entire string to
uppercase.
• Function: def get_msg(): return "hello world"
• Expected Output: HELLO WORLD
'''
# def get_msgs(gm):
#     def wrapper():
#         return gm().upper()
#     return wrapper
#
# @get_msgs
#
# def get_msg():
#     return 'hello world'
# print(get_msg())

'''6th question
6) Call Counter
Create a decorator that tracks how many times a function has been called. It should print the
count every time the function is executed.
• Expected Output: * Called 1 time
o Called 2 times
7) Prefix ID Decorator
Create a decorator that adds the prefix "ID: " to any name returned by a function.
• Function: def get_name(): return "Ravi"
• Expected Output: ID: Ravi
'''

# def func_called(func):
#     c=0
#     def wrapper():
#         nonlocal  c
#         c+=1
#         print('Function Called ',c)
#         func()
#     return wrapper
#
# @func_called
# def func():
#     print('Hello')
# func()
# func()
# func()


'''7th question
7) Prefix ID Decorator
Create a decorator that adds the prefix "ID: " to any name returned by a function.
• Function: def get_name(): return "Ravi"
• Expected Output: ID: Ravi
'''

# def add_prefix(func):
#     def wrapper(*args,**kwargs):
#         name=func(*args,**kwargs)
#         print(f'ID: {name}')
#     return wrapper
# @add_prefix
# def name(n):
#     return n
# name('Anil')

'''8th question
8) The Double Message Wrapper
Create a decorator that prints "Initializing..." before the function starts and "Cleanup Complete"
immediately after it finishes.
• Expected Output: * Initializing...
o [Function Logic Runs]
o Cleanup Complete
'''

# def double_msg_wrapper(func):
#     def wrapper():
#         print('Initializing...')
#         func()
#         print('Cleaned Up')
#     return wrapper
# @double_msg_wrapper
# def dmw():
#     print('[Function Logic Runs]')
# dmw()

'''9th question
9) Negative Result Blocker
Create a decorator for a subtraction function. If the final result is a negative number, the
decorator should return 0 instead.
• Expected Output: (If result is -5) 0
'''

# def subtract(func):
#     def wrapper(*args,**kwargs):
#         ans=func(*args,**kwargs)
#         if ans<0:
#             return 0
#         return ans
#     return wrapper
#
# @subtract
# def sub(x,y):
#     return x-y
#
# x=int(input())
# y=int(input())
# print(sub(x,y))

'''10th question
10) Input Type Validator
Create a decorator that checks the argument of a function. If the argument is not a string, it
should print "Error: Invalid Input Type" and not execute the function.
• Expected Output: Error: Invalid Input Type (if an integer is passed).
'''
# def check_str(func):
#     def wrapper(arg):
#         if type(arg)!=str:
#             print('Error: Invalid Input Type')
#             return
#         return func(arg)
#     return wrapper
# @check_str
# def msg(m):
#     print(m)
# msg('Good Morning')
# msg(8754)



# import time
#
# def calc_time(f):
#     def wrapper(*args,**kwargs):  #arguments are zipped in tuple format
#         print('function called')
#         s=time.time()
#         f(*args,**kwargs) #arguments are unzipped
#         print(f'function end time took {time.time()-s}')
#     return wrapper
#
#
#
# @calc_time
# def fun(x,y,z):
#     print(x+y-z)
# fun(3,4,6)