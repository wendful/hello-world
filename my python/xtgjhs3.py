#系统高阶函数
#filter函数；过滤函数，对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
#调用格式；filter(f,date),f表示是过滤函数，l表示数据
def isEven(a):
	return a%2 == 0
l = [1,2,3,4,5,6,7,8,9]
rst = filter(isEven,l)
#打印出来的是类型，表示是一个可迭代的对象
print(rst)
#对于可迭代的对象，可以如下将它显示出来
print([i for i in rst])
