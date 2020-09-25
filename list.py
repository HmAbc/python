# -*- utf-8 -*-

# 1.一个产品，需要列出产品的用户，这时候就可以使用一个list来表示
user = ['liangdianshui', 'twowater', '两点水']
print('1.产品用户')
print(user)

# 2.如果需要统计有多少个用户，这时候len()函数就可以获得list里的元素个数
len(user)
print('\n2.统计有多少用户')
print(len(user))

# 3.此时，如果需要知道具体的用户呢？可以用索引来访问list中每一个位置的元素，索引是从0开始的
print('\n3.查看具体的用户')
print(user[0] + ',' + user[1] + ',' + user[2] )

# 4.
user.append('茵茵')
print('\n4.在末尾添加新用户')
print(user)

# 5.
user.insert(0, 'VIP用户')
print('\n5.指定位置添加用户')
print(user)

# 6.
user.pop()
print('\n6.删除末尾用户')
print(user)

# 7.
user.pop(1)
print('\n7.删除指定位置的list元素')
print(user)

# 8.
user[2] = '三点水'
print('\n8.把某个元素替换成别的元素')
print(user)

# 9.
newUser = [['VIP用户', 11111], ['twowater', 22222], ['三点水', 33333]]
print('\n9.不同元素类型的list数据')
print(newUser)