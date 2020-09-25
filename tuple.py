#!/user/bin/env python3
# -*- coding: utf-8 -*-

list1 = [123, 456]
tuple1 = ('两点水', 'liangdianshui', 'twowater', list1)
print(tuple1)
list1[0] = 789
list1[1] = 100
print(tuple1)
print(tuple1[3][1])

print('liangdianshui' in tuple1)