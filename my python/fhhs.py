#返回函数
#函数可以返回具体值，也可以返回一个函数作为结果
def myF1():
	def myF2():
		print('我在这里')
		return 3
	return myF2
#将函数myF1赋值给f3，调用f3，返回的是函数myF2	
f3 = myF1()
print(f3)
f3()

def myF4(*args):
	def myF5():
		rst = 0
		for n in args:
			rst +=n
		return rst
	return myF5
#f5是myF4的实例，但返回的结果是myF5	
f5 = myF4(1,2,3,4,5,6,7,8,9)
f5()
print(f5())
		