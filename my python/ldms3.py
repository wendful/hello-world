#类的常用魔术方法
#__str__:当对象被当作字符串时调用
class A():
	def __init__(self,name=0):
		print('lilei')
	def __str__(self):
		return'lilei'
a = A()
#a被当作字符串使用，自动调用__str__函数
print(a)		