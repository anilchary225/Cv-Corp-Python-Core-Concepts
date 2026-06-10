#  Write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of
# characters in the file.
#
# with open('sample.txt','r') as f:
#     content=f.read()
# print('Number of characters : ',len(content))



# • Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10
# characters.

# with open('sample.txt','r') as f:
#     lines=f.readlines()
# for line in lines:
#     if len(line.strip())>10:
#         print(line.strip())

# • Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints
# the complete file content.

# with open('data.txt','w') as f:
#     f.write('this is from q and a from file handling\n')
#     f.write('test 1\n')
#     f.write('test 2\n')
# with open('data.txt','a') as f:
#     f.write('append 1\n')
#     f.write('append 2\n')
# with open('data.txt','r') as f:
#     print(f.read())

# • Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.

# with open('data.txt','r') as f:
#     first_part = f.read(10)
#     print('First 10 Characters: ', first_part)
#
#     print('Cursor position: ',f.tell())
#
#     f.seek(0)
#     print('\nfull content: \n')
#     print(f.read())

# • Create a custom context manager using a class that opens a file in write mode
# in the __enter__ method, writes a line to the file, closes the file in the
# __exit__ method, and properly prints or logs any exception information received
# in __exit__.

# class file_manager:
#     def __init__(self,filename):
#         self.filename=filename
#
#     def __enter__(self):
#         self.file=open(self.filename, 'w')
#         self.file.write('hello this is from class file manager\n')
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#         if exc_type:
#             print('exception type: ',exc_type)
#             print('exception value: ',exc_val)
#         print('file closed successfully')
#         return False
# with file_manager('custom.txt') as f:
#     f.write('Another line from context manager')

# • Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object, and ensures the file is closed
# even if an exception occurs.

# from contextlib import contextmanager
# @contextmanager
# def open_file(filename,mode):
#     f=open(filename,mode)
#     try:
#         yield f
#     finally:
#         f.close()
#         print('file closed')
# with open_file('custom.txt','r') as f:
#     print(f.read())

# • Write a program using a context manager that opens a file in read mode, uses a
# loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(), uses seek() to move to
# a specific position, and continues reading from there.

# with open('custom.txt','r') as f:
#     while True:
#         chunk=f.read(5)
#         if not chunk:
#             break
#         print('Data: ',chunk)
#         print('cursor position: ',f.tell())
#     print(' cursor moving to a specific position 3\n')
#     f.seek(3)
#     print('all data: ',f.read())