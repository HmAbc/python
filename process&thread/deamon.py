#!/user/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import time

# 根据输出结果可见，如果在子进程中添加了 daemon 属性，那么当主进程结束的时候，子进程也会跟着结束
def worker(interval):
    print('工作开始时间：{}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结束时间：{}'.format(time.ctime()))

# 结合上面的例子继续，如果我们想要让子线程执行完该怎么做呢？
#
# 那么我们可以用到 join 方法，join 方法的主要作用是：阻塞当前进程，
# 直到调用 join 方法的那个进程执行完，再继续执行当前进程。
if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    p.join()
    print('End!!')