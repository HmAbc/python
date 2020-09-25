#!/user/bin/env python3
# -*- coding: utf-8 -*-

list1 = [123, 456, 789]
set1 = set(list1)

set2 = set('hello')
set3 = set(['p', 'y', 't', 'h', 'o', 'n'])

print(set2)
print(set3)

# 交集
set4 = set2 & set3
print('\n交集 set4:')
print(set4)

# 并集
set5 = set2 | set3
print('\n并集 set5:')
print(set5)

# 差集
set6 = set2 - set3
set7 = set3 - set2
print('\n差集 set 6:')
print(set6)
print('\n差集 set 7:')
print(set7)

# 去除海量列表里重复元素
list2 = [111, 222, 333, 444, 111, 222, 333, 444, 555, 666]
set8 = set(list2)
print('\n去除列表里重复元素 set7:')
print(set8)