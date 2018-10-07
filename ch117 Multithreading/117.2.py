from queue import Queue
import os
import threading
from threading import Thread


# create a data producer
def producer(output_queue, input_queue):
    while True:
        data = input('Parola Segreta ')
        output_queue.put(data)
        data = input_queue.get()
        input_queue.task_done()
        if data == 'OK':
            break
    print("Producer END Pid %s, thread %s" % (os.getpid(), threading.current_thread().name))


# create a consumer
def consumer(input_queue, output_queue):
    while True:
        # retrieve data (blocking)
        data = input_queue.get()
        input_queue.task_done()
        # do something with the data
        if data == 'END':
            output_queue.put('OK')
            break
        print(data + ' word!  is not defined ')
        output_queue.put('NO NO!')
        # indicate data has been consumed
    print("Consumer END Pid %s, thread %s" % (os.getpid(), threading.current_thread().name))


# Creating producer and consumer threads with a shared queue
q12 = Queue()  # TX-RX
q21 = Queue()  # RX-TX

t1 = Thread(target=consumer, args=(q12, q21))
t2 = Thread(target=producer, args=(q12, q21))
t1.start()
t2.start()
