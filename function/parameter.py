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

# 可变参数，定义函数时，在参数前加一个 * ，表示使用可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

cal = calc(1, 2, 3, 4)
print('使用可变参数序列调用函数: %d' %(cal))

# 如果已经有一个list或tuple，调用一个可变参数函数时，直接在前面加 *
nums = [1, 2, 3]
cal = calc(*nums)
print('存在list，调用一个可变参数的函数：%d' %(cal))

# 强制关键字参数，在要强制使用关键字参数前加 *
def print_user_info(name, *, age, sex = '女'):
    print('昵称:', name, end=' ')
    print('age =', age, end=' ')
    print('sex =', sex)

# 下面的调用方式会报错
# print_user_info('张三', sex = '男', age = 18)
# 必须使用下面的调用方法
print_user_info('张三', age=20, sex='男')