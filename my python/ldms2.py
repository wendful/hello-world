#类的魔术方法
#__call__:对象被当做函数时调用
class A():
	def __init__(self,name=0):
		print('lilei')
	#此案例中不写下面这个函数，程序会报错
	def __call__(self):
		print('lihong')
a = A()
#实例被当作函数调用了，自动触发__call__函数
a()		
