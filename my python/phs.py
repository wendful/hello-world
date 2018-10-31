#偏函数
#把字符串转化成十进制的数字
l = int('123456')
print(l)
#求16进制的字符串'123456'，表示成十进制的数字是多少
l1 = int('123456', base = 16)
print(l1)
#新建一个函数，默认输入的字符串16进制，把此字符串返回十进制
def int16(x, base=16):
	return int(x, base)
l2 = int16('123456')
print(l2)
#可以用偏函数functools.partial实现上述函数的功能
#参数固定的函数，相当于一个特定参数的函数体
#functools.partial的作用是，把一个函数某些参数固定，返回一个新函数
import functools
int16 = functools.partial(int, base=16)
l3 = int16('123456')
print(l3)




