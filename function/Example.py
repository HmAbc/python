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