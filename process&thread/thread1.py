#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('Thread {}, @number {}'.format(self.name, i))
            time.sleep(1)

def main():
    print('Start main threading')
    # 创建三个线程
    threads = [MyThread() for i in range(3)]

    # 启动三个线程
    for t in threads:
        t.start()

    # 依次让线程join，主线程将会等待子线程执行完成
    for t in threads:
        t.join()

    print('End main thread')

if __name__ == '__main__':
    main()