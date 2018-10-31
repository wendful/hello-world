#时间模块
#timeit可以执行一个函数，来测量一个函数的执行时间
import timeit
def doIt():
	num = 3
	for i in range(num):
		print('Repeat for {0}'.format(i))
t = timeit.timeit(stmt = doIt, number = 10)
print(t)		