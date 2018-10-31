#列表生成式
a = [1,2,3,4,5,6,7,8,9,10,11,12]
b = [10,20,30,40,50,60,70,80,90]
#列表生成式可以嵌套
#找出a中的偶数生成新的列表c
c = [m for m in a if m%2 == 0]
d = [m+n for m in a for n in b]
print(c)
print(d)
	
	