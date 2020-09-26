#!/user/bin/env python3
# -*- coding: utf-8 -*-

gen = (x * x for x in range(10))  #与创建list的区别在于外层的括号不一样
print(gen)
for num in gen:
    print(num)

# 以函数的形式事先生成器
def my_function():
    for i in range(10):
        yield i

print(my_function())

# 斐波那契数列生成器
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(500):
    print(x, end=' ')