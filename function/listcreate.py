#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 创建list的方式
#
# list生成式语法
# [expr for iter_var in iterable]
# [expr for iter_var in iterable if cond_expr]

# range()函数左闭右开
list1 = list(range(1, 31))
print(list1)

list2 = [x * x for x in range(1, 11)]
print(list2)

list3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list3)

list4 = [(x+1,y+1) for x in range(3) for y in range(4)]
print(list4)

