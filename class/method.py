#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 类方法调用类属性
class Myclass():
    val1 = '两点水'

    @classmethod
    def fun1(cls):
        print('我是 fun1' + cls.val1)

Myclass.fun1()

# 类方法传参
class ClassA():
    val2 = '两点水'

    @classmethod
    def fun1(cls, age):
        print('我是' + cls.val2)
        print('年龄:' + str(age))

ClassA.fun1(19)

# 从内部增加和修改类属性
class ClassB:
    val1 = '三点水'

    @classmethod
    def fun1(cls):
        print('原来的 val1 值为' + cls.val1)
        cls.val1 = input('请输入修改 val1 的值：')
        print('修改后 val1 值为' + cls.val1)
        cls.val2 = input('新增类属性 val2 ，请为它赋值为：')
        print('新增的 val2 值为' + cls.val2)

ClassB.fun1()
ClassB.val1 = input('请输入修改 val1 的值：')
ClassB.fun1()

ClassB.val2 = input('请输入新增类属性 val2 的值：')
print(ClassB.val2)