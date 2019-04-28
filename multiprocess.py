from multiprocessing import Process,Queue
import os,time,random
def write(q):
	print('Process to write: %s'%os.getpid())
	for value in ['A','B','C']:
		print('Put %s to queue...'%value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read: %s'%os.getpid())
	while True:
		value=q.get(True)
		print('Get %s from queue.'%value)

if __name__ == '__main__':
	q=Queue()
	pw=Process(target=write,args=(q,))
	pr=Process(target=read,args=(q,))
	#开启写入进程
	pw.start()
	#开启读进程
	pr.start()
	#等待读取进程结束
	pw.join()
	#读取进程有死循环必须调用停止
	pr.terminate()
