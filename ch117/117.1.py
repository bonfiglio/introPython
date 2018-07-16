# Esempio uso thread
import threading


# definisco blocco codice thread
def codeThread():
    print("Hello threading!")


my_thread = threading.Thread(target=codeThread)  # Creo Thread
my_thread.start()  # Avvio Thread
try:
    my_thread.start()  # Riavvio Thread ===> RuntimeError: threads can only be started once
except RuntimeError:
    print(' threads can only be started once')

# + thread per importare le diverse pagine
try:
    import requests

    t = input(requests.__version__)
    from threading import Thread
    from queue import Queue
    import time
    import os
except ImportError:
    t = input('Install requests Vedi 81.a1.py ')

q = Queue(maxsize=17)


def put_page_to_q(page_num):
    q.put(requests.get('http://fabrizio.phpnet.us/ilcomputer/cpu/%s.html' % page_num))
    print("END Pid %s, thread %s" % (os.getpid(), threading.current_thread().name))
    print('\thttp://fabrizio.phpnet.us/ilcomputer/cpu/%s.html \tTooks: %.2fs ' % (
    page_num, time.time() - starts[page_num]))


def compile(q):
    print("MAIN Pid %s, thread %s" % (os.getpid(), threading.current_thread().name))
    print('\t\tTooks: %.2fs ' % (time.time() - starts[0]))
    # magic function that needs all pages before being able to be executed
    if not q.full():
        raise ValueError
    else:
        print("HO LETTO TUTTE LE PAGINE ")


print('Senza Threads')
starts = {0: time.time()}
start_2 = time.time()
for page_num in range(1, 18):
    starts[page_num] = time.time()
    put_page_to_q(page_num)
print('\t\tTooks: %.2fs ' % (time.time() - start_2))
q = Queue(maxsize=17)
threads = []
starts = {0: time.time()}
for page_num in range(1, 18):
    t = Thread(target=put_page_to_q, args=(page_num,), daemon=True)
    starts[page_num] = time.time()
    t.start()
    threads.append(t)
# Next, join all threads to make sure all threads are done running before
# we continue. join() is a blocking call (unless specified otherwise using
# the kwarg blocking=False when calling join)
for t in threads:
    t.join()
# Call compile() now, since all threads have completed
compile(q)
