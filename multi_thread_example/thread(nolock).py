""""
多线程之“_thread”的使用
1:主线程如果退出，所有的子线程将会被Kill掉（没有线程守护机制，主线程增大睡眠时间保证子线程不被杀掉）
2：因为没有线程守护机制，所以要手动写代码加锁
"""
import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)    # 日志信息基本配置，日志的输出等级是INFO级别


def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)      # 睡眠4秒
    logging.info("end loop0 at " + ctime())


def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)      # 睡眠4秒
    logging.info("end loop1 at " + ctime())


def main():
    logging.info("start all at " + ctime())
    # 运用_thread可以进行多线程:_thread.start_new_thread(fun,args,kwargs=None)
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(5)
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
