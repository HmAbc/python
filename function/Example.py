#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 反向迭代
# Python中有内置的函数reversed()
# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
# 如果两者都不符合，那你必须先将对象转换为一个列表才行
list1 = [1, 2, 3, 4, 5]
for num in reversed(list1):
    print(num, end=' ')
print()

class Countdown:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        #foward iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1
    def __reversed__(self):
        #reverse iterator
        n = self.start
        while n > 0:
            yield n
            n -= 1

for rr in Countdown(30):
    print(rr, end=' ')
print()
for rr in reversed(Countdown(30)):
    print(rr, end=' ')
print()

# 同时迭代多个序列
# zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a，y 来自 b。
# 一旦其中某个序列到底结尾，迭代宣告结束。
names = ['张三', '李四', '王五']
ages = [20, 35, 23]
for name, age in zip(names, ages):
    print(name, age)
# 利用zip()函数，生成dict
dict1 = dict(zip(names, ages))
print(dict1)