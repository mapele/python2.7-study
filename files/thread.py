import time , threading
# 新线程执行的代码:
#def loop():
    #print 'thread %s is running...' % threading.current_thread().name
    #n = 0
    #while n < 5:
        #n = n + 1
        #print 'thread %s >>> %s' % (threading.current_thread().name, n)
        #time.sleep(1)
    #print 'thread %s ended.' % threading.current_thread().name

#print 'thread %s is running...' % threading.current_thread().name
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print 'thread %s ended.' % threading.current_thread().name

# 假定这是你的银行存款:
balance = 5
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    #先获取锁
    lock.acquire()
    try:
        for i in range(100000):
            change_it(n)
    finally:
        #释放锁
        lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

#-----------测试线程死循环使用多核CPU情况-----------------
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1
print ('multiprocessing.cpu_count:', multiprocessing.cpu_count)
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()