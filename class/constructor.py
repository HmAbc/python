#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 定义一个实例时，构造函数就会被调用
# __init__(self) 函数就是初始化函数，也叫构造函数。
class ClassA():
    # 构造函数，会在创建类的实例时自动调用
    def __init__(self):
        print('实例化成功')

    # 析构函数，会在类实例销毁时自动调用
    def __del__(self):
        print('实例化销毁了')

a = ClassA()

del a
