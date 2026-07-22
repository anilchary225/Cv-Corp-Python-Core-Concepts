# from threading import Thread
# import time
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             time.sleep(1)
#             print("Starting Thread", i)
#
# t1=MyThread()
# t2=MyThread()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Main thread")
# #
# import threading
# import time
#
# def worker(delay):
#     for i in range(3):
#         time.sleep(delay)
#         print(f"[{threading.current_thread().name}] Iteration {i}")
#
# t1 = threading.Thread(target=worker, name="Thread-A", args=(1,),daemon=True)
# t2 = threading.Thread(target=worker, name="Thread-B", args=(1,),daemon=True)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Done")
#
# import threading
# import time
#
# def say(msg):
#     print(f"[{threading.current_thread().name}] {msg}")
#
# t = threading.Thread(target=say, args=("Hello from thread!",), name="GreetThread")
# print(f"[Main] Starting {t.name}")
# t.start()
# t.join()
# print("[Main] Thread has finished. Alive?", t.is_alive())

#
# import threading
# counter = 0
# def unsafe_increment(n):
#     global counter
#     for _ in range(n):
#         counter += 1
# t1 = threading.Thread(target=unsafe_increment, args=(1000000,))
# t2 = threading.Thread(target=unsafe_increment, args=(1000000,))
# t1.start()
# t2.start()
# print("Expected counter = 2000000; Actual counter =", counter)

#
# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def safe_increment(n):
#     global counter
#     for _ in range(n):
#         with lock:
#             counter += 1
#
# t1 = threading.Thread(target=safe_increment, args=(1000000,))
# t2 = threading.Thread(target=safe_increment, args=(1000000,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print("Expected counter = 2000000; Actual counter =", counter)
#
#
#
# import threading
# #
# cv = threading.Condition()
# items = []
#
# # Consumer thread
# def consumer():
#     with cv:
#         print("Consumer")
#         while not items:
#             cv.wait()        # wait for an item
#         item = items.pop()
#     print("Consumed", item)

# Producer thread
# def producer(x):
#     with cv:
#         print("Producing", x)
#         items.append(x)
#         print("Produced", x)
#         cv.notify()         # signal that a new item is available
#
# t1 = threading.Thread(target=consumer)
# t2 = threading.Thread(target=producer, args=(5,))
# t1.start(); t2.start()
# t1.join(); t2.join()
#
#
# import threading, time
# start_event = threading.Event()
# def worker(id):
#     print(f"Worker {id} waiting to start")
#     start_event.wait()
#     print(f"Worker {id} started")
# threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
# for t in threads: t.start()
# time.sleep(5)
# print("Main: Ready, set workers free!")
# start_event.set()
#
#
# from threading import Timer
#
# def delayed_action():
#     print("Action executed after delay")
#
# t = Timer(2.0, delayed_action)
# t.start()
#
# import threading, time
#
# def loop_print(name):
#     for i in range(3):
#         time.sleep(0.1)
#         print(f"{name}: {i}")
#
# t1 = threading.Thread(target=loop_print, args=("Thread-1",),daemon=True)
# t2 = threading.Thread(target=loop_print, args=("Thread-2",),daemon=True)
# t1.start(); t2.start()
#
#
# import threading
# from concurrent.futures import ThreadPoolExecutor
#
# def process(x):
#     print(f"Processing {x} in {threading.current_thread().name}")
#     return x * x
# inputs = [1, 2, 3, 4, 5]
# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(process, x) for x in inputs]
#     for f in futures:
#         result = f.result()
#         print("Result:", result)
# #
#
# import threading
# #
# def task():
#     raise ValueError("An error occurred")
#
# t = threading.Thread(target=task)
# t.start()
# print("Main thread still running.")
#
# lock1 = threading.Lock()
# lock2 = threading.Lock()
# def t1():
#     with lock1:
#         print("t1")
#         with lock2:
#             print("inside t1")
# def t2():
#     with lock2:
#         print("t2")
#         with lock1:
#             t1()
#             print("inside t2")
# th1=threading.Thread(target=t1)
# th2=threading.Thread(target=t2)
# th1.start(); th2.start()
# th1.join(); th2.join()
#
# sem = threading.Semaphore(3)
# def task():
#     with sem:
#         print("Using resource")
# event = threading.Event()
# def waiter():
#     event.wait()
#     print("Proceeding")
# def signaler():
#     event.set()
#
#
#
#
#
#
#

# import asyncio
# import time
# #
# async def task(name, delay):
#     print(f"{name} starts at {time.time():.2f}")
#     await asyncio.sleep(delay)
#     print(f"{name} finishes at {time.time():.2f}")
#
# async def main():
#     a=task(name="A", delay=0.5)
#     print(a)
#     await a
#
#     tasks = [asyncio.create_task(task(f"Task-{i}", 1)) for i in range(3)]
#     print(*tasks, sep="\n")
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())
#
# import multiprocessing
# p1=multiprocessing.Process(target=loop_print, name="p1",args=("Process-1",))
# p2=multiprocessing.Process(target=loop_print, name="p2",args=("Process-2",))
# if __name__=="__main__":
#     p1.start(); p2.start(); p1.join(); p2.join()



# Write a Python program that creates a worker thread
# which prints “Hello
# from worker thread” while the main thread prints
# “Hello from main thread”, and
# ensure that the main thread waits for the worker
# thread to finish execution
# before the program exits.

# import concurrent
# import threading
# import time


# import threading
# import time
#
#
# def fun():
#     print("Hello from worker thread")
#     time.sleep(1)
#
# t=threading.Thread(target=fun)
# t.start()
# t.join()
# print("Hello from main thread")


# Write a Python program that creates three separate
# threads where each
# thread prints numbers from 1 to 5,
# and every printed number must be prefixed
# with the name of the thread that printed it,
# such as “Thread-1: 3”.
#
# def fun():
#     for i in range(1,6):
#         print(f"{threading.current_thread().name}: {i}")
# t1=threading.Thread(target=fun,name="Thread1")
# t2=threading.Thread(target=fun,name="Thread2")
# t3=threading.Thread(target=fun,name="Thread3")
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

# Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution.

# def fun(x,y):
#     start = time.time()
#     z=x+y
#     print(z)
#     print(f"{time.time() - start:.2f}")
# t1=threading.Thread(target=fun,args=(1,3))
# t2=threading.Thread(target=fun,args=(2,3))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("end main thread")

# Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.
# counter=0
# def fun():
#     global counter
#     for i in range(100000000):
#         counter+=1
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun)
# t1.start(); t2.start()
# t1.join(); t2.join()
# print(counter)


# Question - 5
# Modify the previous program so that the shared variable counter is updated
# in a thread-safe manner using threading.Lock, and ensure that the final printed
# value of the counter is always correct.
# counter=0
# lock = threading.Lock()

# def fun():
#     global counter
#     for i in range(1000000):
#         with lock:
#             counter+=1
#
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun)
# t1.start(); t2.start()
# t1.join(); t2.join()
# print(counter)

#
# 6. Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished.
# def fun():
#     print("A started")
#     time.sleep(2)
#
# def fun1():
#     print("B started")
#
# t1=threading.Thread(target=fun)
# t2=threading.Thread(target=fun1)
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# print("main thread started")



# 7. Write a Python program in which three worker threads wait until a
# synchronization signal is received, the main thread sleeps for two seconds and
# then signals all waiting threads using an event, after which each worker thread
# prints a message indicating that it has started execution.
# e=threading.Event()
# def fun():
#     print(f"thread name: {threading.current_thread().name} is started")
#     e.wait()
#     print(f"thread name: {threading.current_thread().name} is stopped")
#
# t1=threading.Thread(target=fun,name="Thread-1")
# t2=threading.Thread(target=fun,name="Thread-2")
# t3=threading.Thread(target=fun,name="Thread-3")
# t1.start()
# t2.start()
# t3.start()
# time.sleep(2)
# e.set()
# print("main thread done")

# 8. Write a Python program that creates five threads competing for a shared
# resource, restricts access so that only two threads can enter the critical
# section at the same time using a semaphore, and prints a message whenever a
# thread enters and exits the critical section.
# s=threading.Semaphore(3)
# x=0
# def fun1():
#     global x
#     with s:
#         x+=1
#         print(x)
#         print(f"{threading.current_thread().name} thread done")
#
# t1=threading.Thread(target=fun1,name="Thread-1")
# t2=threading.Thread(target=fun1,name="Thread-2")
# t3=threading.Thread(target=fun1,name="Thread-3")
# t4=threading.Thread(target=fun1,name="Thread-4")
# t5=threading.Thread(target=fun1,name="Thread-5")
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# print("main thread done")



# 9. Write a Python program that starts a daemon thread running an infinite
# loop which repeatedly prints “Running in background”, while the main thread
# sleeps for two seconds and then exits, and observe what happens to the daemon
# thread when the main program terminates.
# def fun():
#     while True:
#         print("infinte loop running")
# t1=threading.Thread(target=fun,name="Thread-1",daemon=True)
# t2=threading.Thread(target=fun,name="Thread-2",daemon=True)
# t1.start()
# t2.start()
#
# print("main thread done")

# 10. Write a Python program using ThreadPoolExecutor with three worker threads
# that submits tasks to compute the square of numbers from 1 to 5 and prints each
# result as soon as the corresponding task complete

# from concurrent.futures import ThreadPoolExecutor
# def fun(x):
#     print(f"inside fun {x}")
#     return x+1
# l=[1,2,3,4,5]
# with ThreadPoolExecutor(max_workers=3) as executor:
#     # futures= [executor.submit(fun, i) for i in l]
#     futures2=executor.map(fun,l)
#     for i in futures2:
#         print(i)