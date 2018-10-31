#对类中的成员增加一些操作，可以用过property完成
class Person():
	def fget(self):
		return self._name*2
	def fset(self,name):
		self._name = name.upper()
	def fdel(self):
		pass
	name = property(fget,fset,fdel)
p = Person()
p.name = 'lilei'
print(p.name)		