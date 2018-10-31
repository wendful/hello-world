#自定义异常
#自定义异常必须是系统异常的子类
class LishiError(ValueError):
	pass
	#print('我就是自定义的异常，我任性')
try:
	print('i love python')
	print('325897')
	raise LishiError
	print('又没完了')
except NameError as e:
	print(NameError)
except ValueError as e:
	print(ValueError)
except Exception as e:
	print('有异常')
finally:
	print('haha,i am back')
