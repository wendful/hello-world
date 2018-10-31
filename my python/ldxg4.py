#类的相关函数
#dir；获取对象的成员列表
class A():
	name = 'lilei'
	age = '20'
	addr = 'ffd'
	print('hello,my name is {0}'.format(name))
print(dir(A))