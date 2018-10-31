#可以通过globals,locals函数显示全局变量和局部变量
a = 1
b = 2
def fun(c,d):
	e = 111
	print('Locals={0}'.format(locals()))
	print('Globals={0}'.format(globals()))
fun(100,200)	
