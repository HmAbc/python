#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 不同类型的对象对同一消息会作出不同的响应
class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print('hello' + self.name)

class UserVip(User):
    def printUser(self):
        print('hello! 尊敬的VIP用户' + self.name)

class UserGeneral(User):
    def printUser(self):
        print('hello, 尊敬的用户' + self.name)

def printUserInfo(user):
    user.printUser()

if __name__ == '__main__':
    uservip = UserVip('张三')
    printUserInfo(uservip)
    usergeneral = UserGeneral('李四')
    printUserInfo(usergeneral)