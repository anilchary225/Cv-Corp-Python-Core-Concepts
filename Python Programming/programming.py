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

l=[1,2,3,4,5,1,2,3,4]
# l.reverse()
# print(l)
r=[]
for i in range(1,len(l)+1) :

    r.append(l[-i])
print(r)
for i in range(1, len(l)):
    l[i],l[len(l)-i] = l[len(l)-i],l[i]
print(l)



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

# 17. Write a program to find the third-largest number in a list.

# l=[1,2,3,4,5,2,3,7,5,8,9,2,0]
# l.remove(max(l))
# l.remove(max(l))
# print(max(l))


# 18. Write a program to sort a list without using any built-in sorting functions.

# l=[1,2,3,4,5,2,3,7,5,8,9,2,0]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<l[j]:
#             l[j],l[i]=l[i],l[j]
# print(l)

# 19. Write a program to find the Nth largest element in a list.

# l = [1,2,3,4,5,2,3,7,5,8,9,2,0]
# n = 3
# unique = list(set(l))
# unique.sort(reverse=True)
# print(unique[n-1])



# 20. Write a program to print the first four smallest missing elements from a list
# Searching

# l = [1,3,4,5,3,5,8,2,0]
# n=4
# h = 0
# count = 0
# while count < n:
#
#     if h not in l:
#         print(h)
#         count += 1
#
#     h += 1


# 21. Write a program to perform linear search on a list.
# 22. Write a program to perform binary search on a sorted list.
# 23. Write a program to return all index positions of a searched element in a list.
# 24. Write a program to check whether a list is sorted or not.

# l = [1,3,4,5,3,5,8,2,0]
# l1=sorted(l)
# if l == l1:print('Sorted')
# else:print('Not sorted')




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
