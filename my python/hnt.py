'''
汉诺塔递归实现
递归函数：函数自己调用自己
n:代表几个盘子
a:代表第1个塔
b:代表第2个塔
c:代表第3个塔

'''
def hano(n, a, b, c):
	if n == 1:
		print(a,'-->',c)
		return None
	if n == 2:
		print(a,'-->',b)
		print(a,'-->',c)
		print(b,'-->',c)
		return None
	#把n-1个盘子，从a塔借助于c塔移到b塔上去	
	hano(n-1, a, c, b)
	print(a,'-->',c)
	#把n-1个盘子，从b塔借助于a塔移到c塔上去
	hano(n-1, b, a, c)
a = 'A'
b = 'B'
c = 'C'
n = 5
hano(n, a, b, c)		