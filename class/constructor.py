#!/user/bin/env python3
# -*- coding: utf-8 -*-

class ClassA():
    # 构造函数，会在创建类的实例时自动调用
    def __init__(self):
        print('实例化成功')

    # 析构函数，会在类实例销毁时自动调用
    def __del__(self):
        print('实例化销毁了')

a = ClassA()
del a