# import threading
#
# def greetings():
#     print('Hello')
# t1=threading.Thread(target=greetings())

import threading

from executing.executing import lock


def course(name):
    for i in range(10):

        print(name,threading.current_thread().name,i)

t1=threading.Thread(target=course,args=('Python',),name='t1')
t2=threading.Thread(target=course,args=('Java',),name='t2')

t1.start()
t1.join()

t2.start()
t2.join()

print('threads completed')
