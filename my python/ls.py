#私有(private)
#私有成员只能在当前类或对象中访问，外部访问报错
#在成员前添加两个下划线即表示私有

class Person():
	name = 'lilei'
	__age = 28
p = Person
print(p.name)
#__age是私有的，不能在外部访问，所以会报错
print(p.__age)	