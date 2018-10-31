#高阶函数
#高阶函数；把函数作为参数使用的函数

def funA():
	print('hello')
funB = funA
#调用funB时，funA是funB的参数
funB()	