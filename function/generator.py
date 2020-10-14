#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在 Python 中，这种一边循环一边计算的机制，称为生成器：generator。
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回 yield 的值。并在下一次执行 next()方法时从当前位置继续运行。
# 通常在 generator 函数中都要对错误进行捕获

gen = (x * x for x in range(10))  #与创建list的区别在于外层的括号不一样
print(gen)
for num in gen:
    print(num, end=' ')
print()

# 以函数的形式事先生成器
# 只需把 print(i) 变成 yield i
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

for x in fibon(2):
    print(x)

# 打印杨辉三角
def triangle():
    l = [1]
    while True:
        yield l
        l.append(0)
        l = [l[i - 1] + l[i] for i in range(len(l))]

n = 0
for t in triangle():
    print(t)
    n += 1
    if n == 10:
        break
