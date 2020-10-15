#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在定义类的时候，可以在括号里写继承的类，如果不用继承类的时候，也要写继承 object 类，
# 因为在 Python 中 object 类是一切类的父类。
class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self._age


class UserInfo2(UserInfo):
    #这里重写了父类的构造函数
    def __init__(self, name, age, account, sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex

if __name__ == '__main__':
    userInfo2 = UserInfo2('两点水', 23, 2343255, '男')
    # 打印所有属性
    print(dir(userInfo2))
    # 打印构造函数中的属性
    print(userInfo2.__dict__)
    print(UserInfo2.get_name())     # 可以直接调用父类的方法

# isinstance() 不仅可以告诉我们，一个对象是否是某种类型，也可以用于基本类型的判断。
    print(isinstance(userInfo2, UserInfo2))
    print(isinstance('liangdianshui', str))