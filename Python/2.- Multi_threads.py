import threading


def a(i=0):
    for x in range(0, 10):
        print(f'Hi, Im Thread {i} in {x} iteration')


def b(i=0):
    for x in range(0, 10):
        print(f'Hi, Im Thread {i} in {x} iteration')


def c(i=0):
    for x in range(0, 10):
        print(f'Hi, Im Thread {i} in {x} iteration')


thread_a = threading.Thread(target=a, args=[1])
thread_b = threading.Thread(target=b, args=(2,))
thread_c = threading.Thread(target=c, kwargs={'i': 3})

thread_a.start()
thread_b.start()
thread_c.start()
