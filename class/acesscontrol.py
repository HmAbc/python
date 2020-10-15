#!/user/bin/env python3
# -*- coding: utf-8 -*-

class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name    # 公开属性，可以公开访问
        self._age = age     # 私有属性，只是python的编程规范，想访问还是可以访问到
        self.__account = account    # 在创建类时，不能直接访问两个下划线的属性，但是还是有方法访问到

    def get_account(self):
        return self.__account

if __name__ == '__main__':
    userinfo = UserInfo('张三', 23, 3454234)
    # 打印所有属性
    print(dir(userinfo))
    # 打印构造函数中的属性
    print(userinfo.__dict__)
    print(userinfo.get_account())
    # 验证双下划线是否有真正的私有属性
    print(userinfo._UserInfo__account)

# 方法的访问控制
# 我们也可以把方法看成是类的属性的，那么方法的访问控制也是跟属性是一样的，
# 也是没有实质上的私有方法。一切都是靠程序员自觉遵守 Python 的编程规范。
#
# 示例如下，具体规则也是跟属性一样的，

class User(object):
    def upgrade(self):
        pass
    def _buy_equipment(self):
        pass
    def __pk(self):
        pass