# coding:utf-8

from time import sleep, time
import gc

def mem(way=1):
    print time()
    for i in range(100000000):
        if way == 1:
            pass
        else:
            del i

    print time()
    if way == 1 or way == 2:
        pass
    else:
        gc.collect()
    print time()

def mem1():
    print time()
    values = range(1)
    print time()
    weights = range(1)
    print time()
    # vw = map(lambda v1, w1: (v1, w1), xrange(10000000), xrange(10000000))
    a = []
    for w1 in xrange(100000000):
        a.append(w1)
    print time()

if __name__ == "__main__":
    '''
    print 'test way 1:just pass'
    mem(way=3)
    sleep(20)
    print 'test way2:just del'
    mem(way=2)
    sleep(20)
    print 'test way3:del, and then gc.collect()'
    mem(way=3)
    sleep(20)
    '''
    mem1()
