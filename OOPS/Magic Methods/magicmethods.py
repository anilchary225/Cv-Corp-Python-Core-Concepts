'''
__new__  creates new object when calling class
__init__ when class called by obj it internally calls new and init if it used in class

__str__  string representation
__repr__  representation

__add__  addition
__radd__  reverse addition

operators:
__contains__  in operator
__sub__  subtraction
__mul__  multiplication *
__truediv__  /
__floordiv__  //
__pow__ **
__gt__ >
__lt__ <
__ge__ >=
__le__ <=

__getattr__
__getattribute__

iterators and generators
__iter__  or manual call iter()
__next__  or manual call by using for loop

__eq__  equal ==
__ne__ not equal !=
__hash__

file Handling
__enter__
__exit__

'''

'''__str__ and __repr__'''

class A:
    def __init__(self,name,age,b):
        self.name=name
        self.age=age
        self.b=b
    def __str__(self):
        return '{},{},{}'.format(self.name,self.age,self.b)
    def __repr__(self):
        return '{}'.format(self.name)
obj=A('Anil',23,'AI')
obj1=A('Abdul',21,'CSE')
print(obj) #Anil,23,AI  this print calls __str__
print([obj,obj1])  #[Anil, Abdul] this calls __repr__  converts it into list format and adds names in it.
print({obj})  #{Anil}  set format
print(obj)  #Anil,23,AI


'''__add__ and __radd__'''
class A:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return A(self.x+other.x)
    def __radd__(self, other):
        return A(self.x+other.x)
    def __str__(self):
        return '{}'.format(self.x)
a=A(2)
b=A(5)
print(a+b)
print(a)

'''__sub__  __mul__  __truediv__ __floordiv__  __pow__'''
class A:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return A(self.x + other.x)
    def __radd__(self, other):
        return A(self.x + other.x)
    def __sub__(self, other):
        return A(self.x-other.x)
    def __mul__(self,other):
        return A(self.x*other.x)
    def __truediv__(self, other):
        return A(self.x/other.x)
    def __float__(self,other):
        return A(self.x//other.x)
    def __pow__(self, power, modulo=None):
        return A(self.x**power.x)
    def __str__(self):
        return '{}'.format(self.x)
a=A(2)
b=A(5)
c=A(10)
d=A(12)
print(b/d)
print(a-b+b/d**a)

'''__gt__ __lt__ __ge__ __le__ '''
class B:
    def __init__(self,x):
        self.x=x
    def __gt__(self, other):
        return self.x>other.x
    def __lt__(self, other):
        return self.x<other.x
    def __ge__(self, other):
        return self.x>=other.x
    def __le__(self, other):
        return self.x<=other.x
    def __eq__(self, other):
        return self.x==other.x
    def __next__(self,other):
        return self.x!=other.x
a=B(12)
b=B(10)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)



