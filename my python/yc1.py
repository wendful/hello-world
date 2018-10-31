'''
异常是在语法和逻辑都正确的前提喜下，出现的问题
在python中，异常是一个类，可以处理和使用
所有异常都是继承自Excepion
'''
try:
	num = int(input('请输入一个数字:'))
	rst = 100/num
	print('计算结果是:{0}'.format(rst))
#当用户输入的内容不是数字或者是零的时候，会提示输入错误，并退出	
except:
	print('oo,你输错了')
	exit()