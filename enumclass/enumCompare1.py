#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 使用 IntEnum 类进行枚举，就支持比较功能
# 通过输出的结果可以看到，枚举类的成员通过其值得大小进行了排序。也就是说可以进行大小的比较。
import enum

class User(enum.IntEnum):
    twowater = 98
    liangdianshui = 30
    tom = 10

try:
    print('\n'.join(s.name for s in sorted(User)))
except TypeError as err:
    print('error: {}'.format(err))