# 类变量 静态方法 类方法

class Student():
    # 类变量
    classVar = 'class_var'

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = ' + self.id + ', name = ' + self.name

    @classmethod
    def f(cls):
        print(cls.classVar)

    @staticmethod
    def s(self):
        print(self)


Student.f()
Student.s('ni')
