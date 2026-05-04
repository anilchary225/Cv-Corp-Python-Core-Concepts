'''iterations and generations'''




# def fun(x):
#     for i in range(1,x):
#         yield i
#
# for i in range(10):
#     print(i)




# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=0
#
#     def __iter__(self):
#         return self
#
#     def is_prime(self,x):
#         for i in range(2,x):
#             if x%i==0:
#                 return False
#         return True
#
#
#     def __next__(self):
#         if self.c+1>=self.b:
#             raise StopIteration
#         for i in range(self.c+1,self.b+1):
#             if self.is_prime(i):
#                 self.c=i
#                 return self.c
#         raise StopIteration
#
# obj=A(10,20)
#
# ''' for loop'''
# # for i in obj:
# #     print(i)
#
# '''custom iter calling'''
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

'''1. Write a custom iterator that prints numbers from 1 to N.'''

# class Numbers:
#     def __init__(self,n):
#         self.n=n
#         self.c=0
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.c>self.n:
#             raise StopIteration
#
#         self.c+=1
#         return self.c
# num=Numbers(10)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

'''2. Create an iterator that returns only even numbers from a given list.'''


# class EvenNumbers:
#     def __init__(self,data):
#         self.index=0
#         self.data=data
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.index<len(self.data):
#             val=self.data[self.index]
#             self.index+=1
#
#             if val%2==0:
#                 return val
#         raise StopIteration
# l=[1,2,3,4,5,6,7,8,9,0]
# en=EvenNumbers(l)
# for i in en:
#     print(i)
'''
3. Implement an iterator that iterates over a string character by character in
 reverse order.'''

# class S:
#     def __init__(self,s):
#         self.s=s
#         self.i=0
#         self.rev=''
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i==len(self.s):
#             raise StopIteration
#         while self.i<len(self.s):
#
#             val=self.s[len(self.s) - self.i-1]
#             self.i+=1
#             self.rev+=val
#         return self.rev
#
# st=S('shiva')
# for i in st:
#     print(i)
#
# print(next(st))
# print(next(st))
# print(next(st))


'''4. Write an iterator that yields elements of a list with their index (don’t use
enumerate).'''
# class ListIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             result = (self.index, self.data[self.index])
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
#
# # Example usage
# lst = ['a', 'b', 'c', 'd']
#
# for i, val in ListIterator(lst):
#     print(i, val)
#
#
# def my_enumerate(data):
#     index = 0
#     for item in data:
#         yield index, item
#         index += 1
#
#
# # Example usage
# lst = [10, 20, 30]
#
# for i, val in my_enumerate(lst):
#     print(i, val)



'''5. Write a generator that yields digits from an integer one by one.'''

# def digit_generator(data):
#     data=str(abs(data))
#     for ch in data:
#         yield int(ch)
# data=93748
# for d in digit_generator(data):
#     print(d)

# class digit_generator:
#     def __init__(self,data):
#         self.data=str(data)
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         digit = int(self.data[self.index])
#         self.index+=1
#         return digit
#
# num=8736483
# dg=digit_generator(num)
# for i in dg:
#     print(i)


'''6. Create a generator that yields cumulative sum of numbers in a list. Example:
 [1,2,3] → 1, 3, 6'''

# def cumulative_sum(l):
#     # index=0
#     sum=0
#     for i in l:
#         sum+=i
#         # index+=1
#         yield sum
# l=[9,4,2,5]
# for i in cumulative_sum(l):
#     print(i)

# class cumulative_sum:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#         self.total=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>=len(self.l):
#             raise StopIteration
#         self.total+= self.l[self.index]
#         self.index+=1
#         return self.total
#
#
# l=[1,3,5,7]
# cs=cumulative_sum(l)
# for i in cs:
#     print(i)


'''7. Implement a generator that yields vowels from a string.'''

# def vowels(s):
#     for ch in s:
#         yield ch
# s='kajhgf'
# for i in vowels(s):
#     print(i)

# class vowels:
#     def __init__(self,s):
#         self.s=s
#         self.index=0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.s):
#             raise StopIteration
#         st=self.s[self.index]
#         self.index+=1
#         return st
# s='dhfghdj'
# for i in vowels(s):
#     print(i)

'''8. Create an iterator that yields words from a sentence one by one.'''

# def words(s):
#     for w in s.split():
#         yield w
# for w in words('this is the best code'):
#     print(w)

# class words:
#     def __init__(self,s):
#         self.s=s.split()
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.s):
#             raise StopIteration
#         word=self.s[self.index]
#         self.index+=1
#         return word
#
# w=words('this is the best code')
# for i in w:
#     print(i)



'''9. Write an iterator that returns characters at even indices of a string.
'''



''' 10. Implement a generator that yields running maximum from a list Example:
 [3,1,4,2] → 3, 3, 4, 4'''

# def running_max(lst):
#     current_max = float('-inf')  # smallest possible start
#
#     for num in lst:
#         if num > current_max:
#             current_max = num
#         yield current_max
#
#
# # Example
# data = [3, 1, 4, 2]
#
# for val in running_max(data):
#     print(val)