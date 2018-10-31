#多继承案例

class Fish():
	def __init__(self,name):
		self.name = name
	def swim(self):
		print('swiming....')

class Bird():
	def __init__(self,name):
		self.name = name
	def fly(self):
		print('fiying.....')

class Person():
	def __init__(self,name):
		self.name = name
	def work(self):
		print('working.....')

class SuperMan(Person,Bird,Fish):
	def __init__(self,name):
		self.name = name

s = SuperMan('dd')
s.swim()
s.fly()
s.work()

