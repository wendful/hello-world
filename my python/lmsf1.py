#类的成员描述符（属性）；在类中对类的成员属性进行的相关操作而创建的方式
class Student():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		#自己调用自己
		self.setName(name)
	def into(self):
		print('hi my name is {0}'.format(self.name))
	def setName(self,name):
		#名字大写
		self.name = name.upper()
s1 = Student('lilei',12)
print(s1.name)
s1.into()		