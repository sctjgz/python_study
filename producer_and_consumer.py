import time,random
import queue,threading

q = queue.Queue(4)

def Producer(name):
    count = 0
    while True:
        time.sleep(random.randrange(3))
        if q.qsize()<4:
            q.put(count)
            print('Producer %s has produced %d products' % (name,count))
            count+=1

def Consumer(name):
    count = 0
    while True:
        time.sleep(random.randrange(4))
        if not q.empty():
            data = q.get()
            print(data)
            print('Counsumer %s has get %d products' %(name,count))
        else:
            print('There is no products!wuwuwu~')
        count +=1

p1 = threading.Thread(target=Producer,args=('A',))
c2 = threading.Thread(target=Consumer,args=('B',))
c3 = threading.Thread(target=Consumer,args=('C',))

p1.start()
c2.start()
c3.start()