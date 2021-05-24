""""
多线程之“threading”的使用
1：两个线程的执行没有先后顺序


"""
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)    # 日志信息基本配置，日志的输出等级是INFO级别

loops = [2, 4]       # 2秒和4秒：循环的睡眠时间


def loop(nloop, nsec):
    logging.info("start loop" + nloop + " at " + ctime())
    sleep(nsec)      # 睡眠4秒
    logging.info("end loop0" + nloop + " at " + ctime())


def main():
    logging.info("start all at " + ctime())
    nloops = range(len(loops))   # 循环数
    threads = []
    for i in nloops:    # 确定要执行多线程的对象
        t = threading.Thread(target=loop, args=(nloops, loops[i]))
        threads.append(t)
    for i in nloops:    # 启动多线程对象
        threads[i].start()
    for i in nloops:
        threads[i].join()    # 直至启动的线程终止之前一直挂起：除非废除了timeout(秒)，否则会一直阻塞
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
