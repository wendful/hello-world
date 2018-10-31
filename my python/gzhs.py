#构造函数，继承构造函数
class Animal():
	def __init__(self):
		print('Animal')
class buruAni(Animal):
	def __init__(self,name):
		print('buru dongwu{0}'.format(name))
class Dog(buruAni):
	# __init__就是构造函数
	#每次实例化的时候，第一个被自动调用
	#因为主要工作是进行初始化，所以得名
	def __init__(self):
		print('I am init in dog')
#Dog自己有构造函数，所以查找到参数匹配，不报错		
kaka = Dog()

class Cat(buruAni):
	pass
#因为Cat没有自己的构造函数，所以查找父类的
#父类的构造函数带参数，则构造对象时应该按父类参数构造
c = Cat('name')
