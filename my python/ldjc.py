#继承案例
class Person():
	name = 'lile'
	age = 22
	def sleep(self):
		print("sleeping...")
class Teacher(Person):
	pass
t = Teacher()
#Teacher是Person的子类，所以以下两行代码执行结果一样
print(t.name)
print(Person.name)	