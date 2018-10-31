#类的运算类相关魔术方法
#__get__:进行大于判断的时候触发的函数
class Student():
	def __init__(self,name):
		self._name = name
	def __get__(self,obj):
		print('你好,{0}会比{1}大吗'.format(self,obj))
		return self._name>obj._name
stu1 = Student('lilei')
stu2 = Student('liulei')
#返回的是布尔值
print('stu1'>'stu2')		