#!/user/bin/env python3
# -*- coding: utf-8 -*-

def sum(sum1, sum2):
    "返回两数之和"
    if not (isinstance(sum1, (int, float)) and isinstance(sum2, (int, float))):
        raise TypeError('参数类型错误')
    return sum1 + sum2

print(sum(2, 5))

