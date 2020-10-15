#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 类的实例化
# 相比于直接使用类，类方法里面没有了 @classmethod 声明了，不用声明他是类方法
# 类方法里面的参数 cls 改为 self
# 类的使用，变成了先通过 实例名 = 类() 的方式实例化对象，为类创建一个实例，
# 然后再使用 实例名.函数() 的方式调用对应的方法 ，使用 实例名.变量名 的方法调用类的属性
# 而且 self 是所有类方法位于首位、默认的特殊参数。
class ClassA():
    val1 = '两点水'

    def fun1(self):
        print('我是 fun1' + self.val1)

# 实例化
a = ClassA()
a.fun1()        #调用实例的方法
print(a.val1)   #访问实例的属性

# 下面重写类方法
def newFun1(self):
    print('走过路过不要错过哦')

# 重写类方法后，实例的方法会改变，但是无法重写实例方法
ClassA.fun1 = newFun1
a.fun1()

# 类属性改变了，实例属性会跟着改变。
# 但是改变实例中的属性，类属性不会改变
ClassA.val1 = '三点水'
print(a.val1)
