#系统高阶函数
#map；原意是映射，即把集合或者列表的元素按照一定规则进行操作，
#生成一个新的集合或者列表
#如下案例，把列表l1中的元素乘以10，生成新的列表l2，可以如下写
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
	l2.append(i*10)
print(l2)
#以上案例，可以用系统高阶函数map实现
def mulTen(n):
	return n*10
l3 = map(mulTen,l1)
#直接printl3，会显示成为map类
#print(l3)
#所以可以用for遍历
for i in l3:
	print(i,end=' ')
