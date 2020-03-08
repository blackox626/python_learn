import threading
import time


class Account:
    def __init__(self, a_no, balance):
        self.a_no = a_no
        self._balance = balance
        self._lock = threading.RLock()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def draw(self, count):
        self._lock.acquire()
        try:

            if self._balance > count:
                time.sleep(0.001)
                self._balance -= count
                print(f'now:{self._balance}')
            else:
                print('not enough')

        finally:
            self._lock.release()


a = Account('1', 1000)

a.balance = 1200
print(a.balance)


def draw(account, count):
    account.draw(count)


threading.Thread(target=draw, args=(a, 800)).start()
threading.Thread(target=draw, args=(a, 800)).start()
