#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 枚举模块定义了具有迭代 (interator) 和比较(comparison) 功能的枚举类型。
# 它可以用来为值创建明确定义的符号，而不是使用具体的整数或字符串

from enum import Enum, unique

Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# @unique 装饰器可以帮助我们检查保证没有重复值
@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September '
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'

if __name__ == '__main__':
    print(Month.Jan, '---------', Month.Jan.name, '---------', Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '---------', member, '---------', member.value)