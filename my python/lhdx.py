'''
类和对象的三种方法
1.实例方法；需要实例化才能使用
2.静态方法；不需要实例化，通过类直接访问
3.类方法；不需要实例化
'''
#实例化方法
class Person():
	def eat(self):
		print('eating....')
	#静态方法
	#不需要用第一个参数表示自身	
	@staticmethod
	def say():
		print('saying...')
	#类方法
	#第一个参数，一帮命名为cls，区别于self		
	@classmethod
	def play(cls):
		print(cls)
		print('playing...')

p = Person()
p.eat()
Person.say()
Person.play()
#实例化也可以调用静态方法
p.say()	

