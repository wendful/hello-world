#系统高阶函数
#sorted；排序，把一个序列按照给定算法进行排序
a = [256,325,126,4589,12548,332514]
#按照升序，即从小到大排列
al = sorted(a)
print(al)
#按照反序，即从大到小排列。reverse；反序
al1 = sorted(a, reverse = True)
print(al1)
b = [-1,25,-89,65,28]
#按照绝对值的反序排列，abs表示绝对值
bl = sorted(b, key=abs, reverse=True)
print(bl)
#列表中的元素是字符串，也可以调用sorted函数进行排序
astr = ['lilei', 'Haha', 'hanmeimei', 'Liucing']
str1 = sorted(astr)
print(str1)
str2 = sorted(astr, key=str.lower)
print(str2)
