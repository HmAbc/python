#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 因为枚举成员不是有序的，所以它们只支持通过标识(identity) 和相等性 (equality) 进行比较
from enum import Enum

class User(Enum):
    twowater = 98
    liangdianshui = 30
    tom = 10

twowater = User.twowater
liangdianshui = User.liangdianshui
print(twowater == User.liangdianshui, twowater == User.twowater)
print(twowater is User.liangdianshui, twowater is User.twowater)

# 可以看看最后的输出结果，报了个异常，那是因为大于和小于比较运算符引发 TypeError 异常。
# 也就是 Enum 类的枚举是不支持大小运算符的比较的。
try:
    print('\n'.join('  ' + s.name for s in sorted(User)))
except TypeError as err:
    print('error: {}'.format(err))


