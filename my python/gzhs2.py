class A():
	pass

class B(A):
	def __init__(self,name):
		self.name = name
		print('B')

class C(B):
	#c想扩充功能，有两种方法
	#第一种
'''
	def __init__(self,name):
		B. __init__(self,name)
		print('这是c中附加的功能')
'''
#第二种方法，使用super调用
	def __init__(self,name):
		#首先调用父类构造函数
		super(C, self).__init__(name)
		#再增加自己的功能
		print('这是c中附加的功能')
c = C('我是c')    	
