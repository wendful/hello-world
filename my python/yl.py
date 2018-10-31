#元类；用类创造类的类
#元类写法是固定的，必须继承自type
#元类一般命名以MetaClass结尾
class TulingMetaClass(type):
	def __new__(cls, name, bases, attrs):
		#自己的业务处理
		print('hahaha...')
		attrs['id'] = '0001'
		attrs['addr'] = '3458971'
		return type.__new__(cls, name, bases, attrs)
#元类定义完就可以使用		
class Teacher(object, metaclass = TulingMetaClass):
	def work(self):
		print('working...')
t = Teacher()
print(t.id)
print(t.addr)
t.work()
