'''
递归案例
斐波拉契数列：一列数字，第一个值是1，第二个也是1，第三个数是前两个数的和，以此内推
数学公式：f(1)=1,f(2)=1,f(3)=2...f(n)=f(n-1)+f(n-2)
'''
def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fib(n-1)+fib(n-2)
#求第6个数的值	
print(fib(6))		