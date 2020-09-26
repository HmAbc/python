#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 1、循环迭代字符串
for char in 'liangdianshui':
    print(char, end = ' ')

print('\n')

# 2、for循环迭代list
lista = [1, 2, 3, 4, 5]
for num1 in lista:
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

# 如果list里面一个元素有两个变量，也是很容易迭代的
for x, y in [(1, 'a'), (2, 'b'), (3, 'c')]:
    print(x, y)

# 迭代器
# 1、字符创建迭代器对象
str1 = 'liangdianshui'
iter1 = iter(str1)

# 2、list对象创建迭代器
list1 = [1, 2, 3, 4]
iter2 = iter(list1)

# 3、tuple对象创建迭代器
tuple1 = (1, 2, 3, 4)
iter3 = iter(tuple1)

# for循环便利迭代器
for x in iter1:
    print(x, end = ' ')
print('\n------------------')

# next()函数遍历迭代器
while True:
    try:
        print(next(iter3))
    except StopIteration:
        break
