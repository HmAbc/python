#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 匿名函数主要有以下特点：
#
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

# lambda [arg1 [,arg2,.....argn]]:expression

# 示例
sum = lambda num1, num2 : num1 + num2;
print(sum(1, 2))

#  lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，而不是定义时就绑定
num2 = 100
sum = lambda num1 : num1 + num2;
print(sum(1))

num2 = 10000
sum = lambda num1 : num1 + num2;
print(sum(1))