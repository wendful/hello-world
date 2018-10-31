#扩充父类功能
class Person():
	name = 'noname'
	age = 30
	__score = 22
	_petname = 'lier'
	def sleep(self):
		print('sleering...')
	def work(self):
		print('maek some money')

class Teacher(Person):
	teacher_id = '9527'
	name = "dada"
	def make_test(self):
		print('attention')
	def work(self):
		#扩充父类的功能只需要调用父类相应的函数
		#Person.work(self)
		#还可以用super()代表父类
		super().work()
		self.make_test()

t = Teacher()
t.work()						