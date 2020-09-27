#!/user/bin/env python3
# -*- coding: utf-8 -*-

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for x in reversed(Countdown(30)):
    print(x, end = ' ')

print()

for x in Countdown(30):
    print(x, end = ' ')
print()

# 同时迭代两个序列
names = ['liangdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
for x, y in zip(names, ages):
    print(x, y)

# 使用zip()函数，把一个name列表和age列表生成dict
dict1 = dict(zip(names, ages))
print(dict1)
