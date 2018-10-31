#类的常用魔术方法
#__setattr__:对成员属性进行设置时触发
class Person():
	def __init__(self):
		pass
	def __setattr__(self,name,value):
		print('{0}'.format(name))
		#self.name = value
		super().__setattr__(name,value)
p = Person()
#print(p.__dict)
p.age = 18	    	
