#异常案例
#给出提示信息
try:
	num = int(input('请输入一个非零数字:'))
	rst = 100/num
	print('计算结果是{0}'.format(rst))
#捕获异常后，把异常实例化，并显示在实例中
#以下语句是捕获ZeroDivisionError异常并实例化e
#ZeroDivisionError是一种错误类型，除零错误	
except ZeroDivisionError as e:
	print('你的输入有问题')
	print(e)
	exit()

