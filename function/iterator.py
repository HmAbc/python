#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 1、循环迭代字符串
for char in 'liangdianshui':
    print(char, end = ' ')

print('\n')

# 2、for循环迭代list
list1 = [1, 2, 3, 4, 5]
for num1 in list1:
    print(num1, end = ' ')
print('\n')

# 3、for循环也可以迭代dict
dict1 = {'name':'两点水', 'age':'23', 'sex':'男'}
for key in dict1:       # 迭代dict中的key
    print(key, end = ' ')
print('\n')

for value in dict1.values():
    print(value, end = ' ')
print('\n')