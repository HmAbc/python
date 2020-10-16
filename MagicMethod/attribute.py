#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在 Python 中，所有以 "" 双下划线包起来的方法，都统称为"魔术方法"
# 我们可以使用 Python 内置的方法 dir() 来列出类中所有的魔术方法
# __new__ 是用来创建类并返回这个类的实例, 而__init__ 只是将传入的参数来初始化该实例.
# __new__ 在创建一个实例的过程中必定会被调用,但 __init__ 就不一定，
# 比如通过 pickle.load 的方式反序列化一个实例时就不会调用 __init__ 方法。
# def __new__(cls) 是在 def __init__(self) 方法之前调用的，作用是返回一个实例对象。
# 还有一点需要注意的是：__new__ 方法总是需要返回该类的一个实例，而 __init__ 不能返回除了 None 的任何值
class User(object):
    def __getattr__(self, name):
        print('调用了 __getattr__ 方法')
        return super(User, self).__getattr__(name)

    def __setattr__(self, name, value):
        print('调用了 __setattr__ 方法')
        return super(User, self).__setattr__(name, value)

    def __delattr__(self, name):
        print('调用了 __delattr__ 方法')
        return super(User, self).__delattr__(name)

    def __getattribute__(self, name):
        print('调用了__getattribute__方法')
        return super(User, self).__getattribute__(name)

if __name__ == '__main__':
    user = User()
    # 设置属性值，会调用 __setattr__
    user.attr1 = True
    # 属性存在，只有 __getattribute__ 调用
    user.attr1
    try:
        # 属性不存在，先调用 __getattribute__, 后调用 __getattr__
        user.attr2
    except AttributeError:
        pass
    # __delattr__ 调用
    del user.attr1