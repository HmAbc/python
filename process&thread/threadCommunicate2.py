#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 设置信号
# 使用 Event 的 set() 方法可以设置 Event 对象内部的信号标志为真。
# Event 对象提供了 isSe() 方法来判断其内部信号标志的状态。
# 当使用 event 对象的 set() 方法后，isSet() 方法返回真
#
# 清除信号
# 使用 Event 对象的 clear() 方法可以清除 Event 对象内部的信号标志，
# 即将其设为假，当使用 Event 的 clear 方法后，isSet() 方法返回假
#
# 等待
# Event 对象 wait 的方法只有在内部信号为真的时候才会很快的执行并完成返回。
# 当 Event 对象的内部信号标志位假时，则 wait 方法一直等待到其为真时才返回。

import threading

class mThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        # 使用全局event
        global event
        if event.isSet():
            event.clear()
            event.wait()
            print(self.getName())
        else:
            print(self.getName())
            event.set()

event = threading.Event()

event.set()
t1 = []
for i in range(10):
    t1.append(mThread(str(i)))

for i in t1:
    i.start()