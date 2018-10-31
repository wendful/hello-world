#手动引发异常
#用raise关键字手动引发异常
try:
	print('我喜欢python')
	print('3.1415926')
	#手动引发一个异常
	#语法；raise ErrorClassName
	raise ValueError
	print('还有完没完了')
except NameError as e:
	print('NameError')
except ValueError as e:
	print('ValueError')
except Exception as e:
	print('有异常')
finally:
	print('我肯定会被执行的')