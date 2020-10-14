#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象。
def change_num(b):
    print('函数中一开始b的值：{}'.format(b))
    b = 1000
    print('函数中b赋值后的值：{}'.format(b))

b = 1
change_num(b)
print('调用函数后的b的值：{}'.format(b), end='\n\n')

# 作为比较传递一个list进入函数
def change_list(b):
    print('函数中一开始b的值：{}'.format(b))
    b.append(1000)
    print('函数中b增加后的值：{}'.format(b))

c = [1, 2, 3, 4, 5]
change_list(c)
print('调用函数后list的值为：{}'.format(c))