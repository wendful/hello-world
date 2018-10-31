'''
把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
定义时，用*args表示
'''
def student(*args):
	print("hello 大家好")
	for i in args:
		print(i)
	
student('lilei', 18, 'son')	