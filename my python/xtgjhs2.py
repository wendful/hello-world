#系统高阶函数
#reduce；原意是归并缩减，把一个课迭代对象最后归并成一个结果
#使用reduce函数需要导入functools包
from functools import reduce
def myAdd(x,y):
	return x+y
rst = reduce(myAdd,[1,2,3,4,5,6])
print(rst)
#so 求1加到100的和的代码可以如下写
rst2 = reduce(myAdd,[i for i in range(1,101)])
print(rst2)	