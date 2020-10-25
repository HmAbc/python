#!/user/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os, random, time

def write(q):
    print('写进程的PID：{}'.format(os.getpid()))
    for value in ['两点水', '三点水', '四点水']:
        print('写进Queue的值为：{}'.format(value))
        q.put(value)
        time.sleep(random.random() * 2)

def read(q):
    print('读进程的PID：{}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从Queue读取的数据为：{}'.format(value))

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
