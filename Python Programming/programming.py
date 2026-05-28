'''
Basic List Questions
'''
#
# 1. Write a program to create a list by taking input from the user and print the list.

# l=list(map(int,input().split()))
# print(l)

# 2. Write a program to insert an element at a specific index in a list.

# l=[1,2,3,4,5,6,7]
# l.insert(2,10)  #shifts the elements to forward 1 position
# print(l)

# 3. Write a program to merge two lists into a single list.

# l1=[2,3,4]
# l2=[5,6,7]
# print(l1+l2)

# 4. Write a program to remove a specific element from a list.

# l=[1,2,3,4]
# l.remove(1)
# print(l)
# l.pop()
# print(l)

# 5. Write a program to remove an element from a list using its index.

# l=[1,2,3,4]
# l.pop(2)
# print(l)

# 6. Write a program to find the index of a given element in a list.

# l=[1,2,3]
# print(l.index(3))

# 7. Write a program to count the number of occurrences of an element in a list.

# l=[1,2,3,4,5,6,2,4,6,7,9,9,76,4,0,4,5,7,7,8,9,6,43,0]
# print(l.count(0))

# 8. Write a program to find the sum of the first and last elements of a list.

# l=[1,2,3,4]
# print(l[0]+l[-1])

# 9. Write a program to calculate the sum of list elements up to a given index.
#
# l=[1,2,3,4,6,7,8]
# n=5
# s=0
# for i in range(n+1):
#     s+=l[i]
# print(s)

# 10. Write a program to calculate the average of odd numbers in a list.

# l=[1,2,3,4,5,6,7,8]
# s=0
# for i in l:
#     if i%2!=0:
#         s+=i
# print(s)

# 11. Write a program to print all prime numbers present in a list.

# l=[1,2,3,4,5,6,7,11,13]
# for i in l:
#     found=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             found=False
#             break
#     if found:
#         print(i,end=' ')



# 12. Write a program to print the next prime number for each element in the list

# l=[1,2,3,4,5,6,7]
# for i in l:
#     found=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             found=False
#             break
#
#     if found:
#         np = i+1
#         while True:
#             next_p=True
#             for j in  range(2,int(np**0.5)+1):
#                 if np%j==0:
#                     next_p=False
#                     break
#             if next_p:
#                 print(np)
#                 break
#             np+=1


# 13. Write a program to print the list in reverse order.

# l=[1,2,3,4,5,1,2,3,4]
# # l.reverse()
# # print(l)
# r=[]
# for i in range(1,len(l)+1) :
#
#     r.append(l[-i])
# print(r)
# for i in range(1, len(l)):
#     l[i],l[len(l)-i] = l[len(l)-i],l[i]
# print(l)



# 14. Write a program to find sum of any two elements which is equal to key value

# n=5
# l=[1,2,3,4,5,6,7,8]
# for i in range(len(l)):
#     for j in range(i+1):
#         if l[i]+l[j]==n:
#             print(l[i],l[j])


# Maximum & Minimum
# 15. Write a program to find the largest number in a list.

# l=[1,2,3,4,5,2,3,7,5,8,9,2,0]
# print(max(l))
# print(min(l))

# 16. Write a program to find the second-largest number in a list.

# l=[1,2,3,4,5,2,3,7,5,8,9,2,0]
# l.remove(max(l))
# print(max(l))

# l=[5,10,2,11,13,13,7,12,3]
# h1=float('-inf')
# h2=h1
# for i in range(len(l)):
#     if l[i]>h1:
#         h2=h1
#         h1=l[i]
#     # elif l[i]>h2 and l[i]<h1:
#     # element -> All values consider only l[i]>h2 ,if number -> No duplicates consider l[i]<h1
#     elif h1>l[i]>h2 :
#         h2=l[i]
#
# print(h2)

# 17. Write a program to find the third-largest number in a list.

# l=[5,10,2,11,13,13,7,12,3]
# h1=float('-inf')
# h2=h1
# h3=h2
# for i in range(len(l)):
#     if l[i]>h1:
#         h2=h1
#         h3=h2
#         h1=l[i]
#     elif h2 >l[i] >h3 :
#         h3=l[i]
# print(h3)

# l=[1,2,3,4,5,2,3,7,5,8,9,2,0]
# l.remove(max(l))
# l.remove(max(l))
# print(max(l))

# Write a program to find the fifth-largest number in a list.

# l=[5,10,2,11,13,13,7,12,3]
# print(sorted(l))
# h1=float('-inf')
# h2=h1
# h3=h2
# h4=h3
# h5=h4
# for i in range(len(l)):
#     if l[i]>h1:
#         h2=h1
#         h3=h2
#         h4=h3
#         h5=h4
#         h1=l[i]
#     elif h2 > l[i] > h3:
#         h3=l[i]
#     elif h3 > l[i] >h4 :
#         h4=l[i]
#     elif h4 > l[i] >h5 :
#         h5=l[i]
# print(h5)

# 18. Write a program to sort a list without using any built-in sorting functions.

# l=[1,2,3,4,5,2,3,7,5,8,9,2,0]
# k=5
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]: #ascending order , l[i]<l[j] for descending order
#             l[j],l[i]=l[i],l[j]
# print(l)
# print(l[-k])


# 19. Write a program to find the Nth largest element in a list.

# l = [1,2,3,4,5,2,3,7,5,8,9,2,0]
# n = 3
# unique = list(set(l))
# unique.sort(reverse=True)
# print(unique[n-1])



# 20. Write a program to print the first four smallest missing elements from a list


# l = list(map(int,input().split()))
#
# h = min(l)+1
# count = 0
# while True:
#
#     if h not in l:
#         print(h)
#         count += 1
#         if count == 4:
#             break
#
#     h += 1

# Searching
# 21. Write a program to perform linear search on a list.

# l=[1,10,5,8,3,12]
# k=5
# found=False
# for i in range(len(l)):
#     if l[i]==k:
#         found=True
#         break
# print('found' if found else 'Not found')


# 22. Write a program to perform binary search on a sorted list.

# l=[1,10,5,8,3,12]
# k=9
#l.sort()
# found=False
# first=0
# last=len(l)-1
# while first<=last:
#     m=(first+last)//2
#     if l[m]==k:
#         found=True
#         break
#     elif k>l[m]:
#         first=m+1
#     else:
#         last=m-1
# print('Found' if found else 'Not Found')

# 23. Write a program to return all index positions of a searched element in a list.
# 24. Write a program to check whether a list is sorted or not.

# l = [1,3,4,5,3,5,8,2,0]
# l1=sorted(l)
# if l == l1:print('Sorted')
# else:print('Not sorted')

# l=[1,2,3,4,5]
# found=True
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:found=False
# print('Sorted' if found else 'Not Sorted')



# Math on arrays
# 25. Write a program to find the LCM of all numbers in the list.

# l=[2,3,4,6,8,56]
# h=max(l)
# k=h
# found = False
# while not found:
#     found=True
#     for i in l:
#
#         if k%i!= 0 :
#             found=False
#             break
#     if not found:
#         k+=h
# if found:
#     print(k)

# 26. Write a program to find the GCD of all numbers in the list.

# l = [12, 24, 36]
# small=min(l)
# for i in range(small,0,-1):
#     found=True
#     for j in l:
#         if j%i!=0:
#             found=False
#             break
#     if found:
#         print(i)
#         break






# 27. Write a program to find the factorial of each element in a list
# Frequency

# l=[1,5,6,3,6,7,8,4,2,5,7,8,9,3,6,7,8]
#
# for i in l:
#     s = 1
#     for j in range(1,i+1):
#         s*=j
#     print('factorial of {} is {}'.format(i,s))


# 28. Write a program to find the frequency of each element in a list.

# l=[1,5,6,3,6,7,8,4,2,5,7,8,9,3,6,7,8]
# for i in l:
#     print('frequency of {} is {}'.format(i,l.count(i)))

# 29. Write a program to calculate the backward frequency of elements in a list.
# 30. Write a program to print frequencies of each element without repetition.
# 31. Write a program to find the most frequently repeated element in a list.

# l=[1,5,6,3,6,7,8,4,2,5,7,8,9,3,6,7,8,5,5,5,5,5,5,5,5,5]
# lf=0
#
# for i in l:
#     if lf<l.count(i):
#         lf=l.count(i)
# print('lf: ',lf)
# for i in l:
#     if l.count(i)==lf:
#         print(i)
#         break


# 32. Write a program to find the unique element in a list.

# l=[1,5,6,3,6,7,8,4,2,5,7,8,9,3,6,7,8]
# l.sort()
# print(l)

# 33. Write a program to find the least unique element in a list.
# 34. Write a program to print elements whose frequency is greater than 1.
# Rotation
# SubLists
# Practice
# 35. Write a program to print all rotations of a list (clockwise)
# 36. Write a program to print all rotations of a list (anticlockwise)
# 37. Write a program to rotate a list by k positions.(anticlockwise)
# 38. Write a program to print all possible sublists of a list.
# 39. Write a program to find all subarrays whose sum is equal to a given key.
# 40. Write a program to print all possible subsequences of a list.
# 41. Write a program to convert a list of digits into a number.
# 42. Write a program to convert a number into a list of digits.
# 43. Write a program to reverse a list and also reverse each element in the list.


'''Password Validation'''

# s = input()
#
# if len(s) == 9:
#
#     uc = lc = dc = False
#     sp = True
#
#     for i in range(len(s)):
#
#         if s[i].isupper():
#             uc = True
#
#         elif s[i].islower():
#             lc = True
#
#         elif s[i].isdigit():
#             dc = True
#
#         else:
#             sp = False
#             break
#
#
#     if uc and lc and dc and sp:
#         print("Valid Password")
#
#     else:
#         print("Invalid")
#
# else:
#     print("Invalid")

'''Pancard Validation'''

# pancard=input()
# k='CHATPF'
# if len(pancard)==10:
#     valid = True
#     for i in range(len(pancard)):
#         if i<=2 or i==4 or i==9 and pancard[i].isupper():
#             continue
#         elif i==3 and pancard[i] in k :
#             continue
#         elif (i>=5 and i<=8) and pancard[i].isdigit():
#             continue
#         else:
#             valid=False
#
#             break
#     if valid :
#         print('Pancard is Valid')
#     else:
#         print('Invalid')
# else:
#     print('Length of pancard must be equal to 10')

'''Vehicle Number Validation'''

# vn=input()
#
# if len(vn)==10:
#     valid = True
#     for i in range(len(vn)):
#         if (i==0 or i==1 or i==4 or i==5) and vn[i].isupper():
#             continue
#         elif (i==2 or i==3 or i==6 or i==7 or i==8 or i==9 ) and vn[i].isdigit():
#             continue
#         else:
#             valid = False
#             break
#     if valid :
#         print('Vehicle number is Valid')
#     else:
#         print('Invalid Vehicle number')
# else:
#     print('Vehicle number must be greater than 10')

