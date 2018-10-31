'''
类的相关函数
issubcalss；判断一个类是否是另一个类的子类
'''
class A():
	pass
class B(A):
	pass
#判断B是不是A的子类
print(issubclass(B,A))	