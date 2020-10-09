#!/user/bin/env python3
# -*- coding: utf-8 -*-

class User(object):
    def __getattr__(self, name):
        print('调用了 __getattr__ 方法')
        return super(User, self).__getattr__(name)

    def __setattr__(self, name, value):
        print('调用了 __setattr__ 方法')
        return super(User, self).__setattr__(name, value)

    def __delattr__(self, name):
        print('调用了 __delattr__ 方法')
        return super(User, self).__delattr__(name)

    def __getattribute__(self, name):
        print('调用了__getattribute__方法')
        return super(User, self).__getattribute__(name)

if __name__ == '__main__':
    user = User()
    # 设置属性值，会调用 __setattr__
    user.attr1 = True
    # 属性存在，只有 __getattribute__ 调用
    user.attr1
    try:
        # 属性不存在，先调用 __getattribute__, 后调用 __getattr__
        user.attr2
    except AttributeError:
        pass
    # __delattr__ 调用
    del user.attr1