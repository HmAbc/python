#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 类的实例化
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

ClassA.fun1 = newFun1
a.fun1()