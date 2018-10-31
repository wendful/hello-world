#异常中的else语句案例
try:
	num = int(input('请输入一个非零数字'))
	rst = 100/num
	print('计算结果是{0}'.format(rst))
except Exception as e:
	print('Exception')
else:
	print('wandfull')
finally:
	print('我又回来了，哈哈哈')
