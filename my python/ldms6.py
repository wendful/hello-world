#类的常用魔术方法
#__getattr__:访问一个不存在的属性时触发
class A():
	name = 'lilei'
	def __getattr__(self,name):
		print('haha')
		print(name)
a = A()
print(a.name)
#addr属性不存在，自动触发__getattr__函数
print(a.addr)		