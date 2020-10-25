#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 这里有一点需要注意： Pool 对象调用 join() 方法会等待所有子进程执行完毕，调用 join() 之前必须先调用 close() ，
# 调用close() 之后就不能继续添加新的 Process 了。
#
# 请注意输出的结果，子进程 0，1，2，3是立刻执行的，而子进程 4 要等待前面某个子进程完成后才执行，
# 这是因为 Pool 的默认大小在我的电脑上是 4，因此，最多同时执行 4 个进程。
# 这是 Pool 有意设计的限制，并不是操作系统的限制。

from multiprocessing import Pool
import os, random, time

def long_time_task(name):
    print('进程的名称：{} 进程的PID：{}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程{}运行了{}秒'.format(name, (end - start)))

if __name__ == '__main__':
    print('主进程的PID：{}'.format(os.getpid()))
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task, args=(i, ))
    p.close()
    p.join()
    print('【end】')