#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 在 Python 中，常见的容器类型有: dict, tuple, list, string。
# 其中也提到过可容器和不可变容器的概念。其中 tuple, string 是不可变容器，dict, list 是可变容器。

class FunctionList:
    # 实现了内置类型list的功能，并丰富了一些其他方法：head，tail，init，last，drop，take
    def __init__(self, values=none):
        if values == none:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 返回第一个值
        return self.values[0]

    def tail(self):
        # 获取第一个值之后的所有元素
        return self.values[1:]

    def init(self):
        # 获取最后一个元素之前的所有元素
        return self.values[:-1]

    def last(self):
        # 获取最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 获取所有元素，除了前n个
        return self.values[n:]

    def take(self, n):
        # 获取前n个元素
        return self.values[:n]
