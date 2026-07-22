# 1. Write a Python program using a context manager (with)
# to open a text file in read mode. Read the complete content of the file and print:
#
# * Total number of lines
# * Total number of words
# * Total number of characters
#

# with open('test.txt','r') as f :
#     lines=f.readlines()
#     l=w=c=0
#     for line in lines:
#         l+=1
#         for words in line.split():
#             w+=1
#             for characters in words:
#                 c+=1
#     print('lines',l)
#     print('words',w)
#     print('characters',c)

#
# 2. Write a program that opens a text file in read mode,
# replaces every occurrence of the word "Python" with "Programming",
# and writes the updated content into a new file using a context manager.
# Finally, display the content of the new file.

# with open('test.txt','r') as f ,open('test2.txt','w') as n:
#     lines=f.readlines()
#     for line in lines:
#         for w in line.split():
#             if w.lower()=='python':
#                 n.write('programming')
#                 n.write(' ')
#             else:
#                 n.write(w)
#                 n.write(' ')



# 3. Write a Python program that opens a text file using a context manager,
# reads all lines using readlines(), and prints only the alternate lines
# (1st, 3rd, 5th, etc.). Also print the total number of alternate lines displayed.

with open('test.txt','r') as f:
    lines=f.readlines()
    c=ac=0
    for line in lines:
        if c%2==0:
            print(line)
            ac += 1
        c+=1

print(ac)