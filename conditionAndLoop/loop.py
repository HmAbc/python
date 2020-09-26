#!/user/bin/env python3
# -*- coding: utf-8 -*-

for x in 'Hello 两点水':
    print(x)

dict1 = {'一点水': '小学生', '两点水': '中学生', '三点水': '高中生'}
for i in dict1:
    print('(' + i + ':' + dict1[i] + ')')

# range(x)函数生成一个从0到x-1的整数序列, range(a, b)生成一个从a到b的左闭右开的整数序列
for i in range(3):
    print(i)

# range函数还有第三个参数，表示步进
for i in range(0, 10 , 2):
    print(i)

count = 1
sum1 = 0

while count <= 100:
    sum1 = sum1 + count
    count = count + 1

print(sum1)

