import threading
import time


class Account:
    def __init__(self, a_no, balance):
        self.a_no = a_no
        self._balance = balance
        self._cond = threading.Condition()
        self._flag = False

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def draw(self, count):
        self._cond.acquire()
        try:
            if not self._flag:
                self._cond.wait()
            else:
                if self._balance > count:
                    self._balance -= count
                    print(f'now:{self._balance}')
                    self._flag = False
                    self._cond.notifyAll()
                else:
                    print('not enough')
        finally:
            self._cond.release()

    def save(self, count):
        self._cond.acquire()
        try:
            if self._flag:
                self._cond.wait()
            else:
                self._balance += count
                self._flag = True
                self._cond.notifyAll()
                print(f'now:{self._balance}')
        finally:
            self._cond.release()


a = Account('1', 1000)


def draw(account, count):
    account.draw(count)


def save(account, count):
    account.save(count)


threading.Thread(target=draw, args=(a, 800)).start()
threading.Thread(target=save, args=(a, 800)).start()
