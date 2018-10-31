#高阶函数
#funA是普通函数，返回值是一个数字的100倍
def funA(n):
	return n*100
#再写一个函数，把传入的参数乘以300
def funB(n):
	return funA(n)*3
print(funB(10))
#写一个高阶函数
def funC(n,f):
	return f(n)*3
print(funC(10,funA))	