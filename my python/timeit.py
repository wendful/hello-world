#时间模块
#timeit；时间测量工具
#sleep(n):使程序进入睡眠，n秒后继续
import time
def p():
	time.sleep(3)
t = time.time()
p()
print(time.time()-t)	