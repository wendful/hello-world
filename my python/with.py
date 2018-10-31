#with语句；使用的技术是一种成为上下文管理协议的技术
with open('C:\\Users\\Administrator\\Desktop\\my python', 'r') as f:
	strline = f.readline()
	while strline:
		print(strline)
		strline = f.strline()
