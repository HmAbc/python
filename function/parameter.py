#!/user/bin/env python3
# -*- coding: utf-8 -*-

def print_user_info(name, age, sex = '男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end = '   ')
    print('年龄：{}'.format(age), end = '   ')
    print('性别：{}'.format(sex))
    return

# 调用 print_user_info 函数

print_user_info('两点水', 18, '女')
print_user_info('三点水', 25)


# 判断默认参数有没有传入，object是python中所有类的基类，可以创建它的实例，只能用来测试同一性

_no_value = object()

def print_info(a, b = _no_value):
    # 测试默认参数有没有传入
    if b is _no_value:
        print('b没有赋值')
    return

print_info(2)


# 可以通过元组方式传入不定长参数

def print_info1(name, age, sex = '男', * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end = '   ')
    print('年龄：{}'.format(age), end = '   ')
    print('性别：{}'.format(sex), end = '   ')
    print('爱好：{}'.format(hobby))
    return

print_info1('两点水', '18', '女', '打篮球', '打羽毛球', '跑步')