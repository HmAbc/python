#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
# 创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。

from queue import Queue
from threading import Thread

isRead = True

def write(q):
    # 写入数据
    for i in ['两点水', '三点水', '四点水']:
        print('写进Queue的值为 {}'.format(i))
        q.put(i)

def read(q):
    while not q.empty():
        value = q.get(True)
        print('从Queue中读取到的值为 {}'.format(value))

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t2 = Thread(target=read, args=(q,))
    t1.start()
    t2.start()

