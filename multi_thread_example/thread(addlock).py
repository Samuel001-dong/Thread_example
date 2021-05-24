""""
多线程之“_thread”的使用
1:主线程如果退出，所有的子线程将会被Kill掉（没有线程守护机制）
2：因为没有线程守护机制，所以要手动写代码加锁
"""
import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)    # 日志信息基本配置，日志的输出等级是INFO级别

loops = [2, 4]       # 2秒和4秒：循环的睡眠时间


def loop(nloop, nsec, lock):
    logging.info("start loop" + nloop + " at " + ctime())
    sleep(nsec)      # 睡眠4秒
    logging.info("end loop0" + nloop + " at " + ctime())
    lock.release()


def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))   # 循环数
    # 获取锁
    for i in nloops:
        lock = _thread.allocate_lock()    # 分配锁
        lock.acquire()                    # 加锁
        locks.append(lock)                # 将锁添加到列表中
    # 依次启动所有线程
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 依次检查所有线程是否结束
    for i in nloops:
        while locks[i].locked():  # 如果检查到锁是一直锁上的则什么都不做（停在此句代码，注意：这里只有loop0解锁之后才会检查loop1）
            pass
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
