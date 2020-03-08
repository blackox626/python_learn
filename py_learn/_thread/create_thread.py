import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i = 0

    def run(self):
        while self.i < 100:
            print(threading.current_thread().name + ":" + str(self.i))
            self.i += 1


def action(count):
    for t in range(count):
        print(threading.current_thread().name + ":" + str(t))


for i in range(100):
    print(threading.current_thread().name + ":" + str(i))
    if i == 2:
        MyThread().start()
        MyThread().start()
        # t1 = threading.Thread(target=action, args=(100,))
        # t1.start()
        # t2 = threading.Thread(target=action, args=(100,))
        # t2.start()

print('main _thread finished')
