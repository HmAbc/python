#!/user/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing
import os, random, time


if __name__ == '__main__':
    print('主进程的PID：{}'.format(os.getpid()))
    p = Pool(4)
    for i in range(6):
