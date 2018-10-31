#exec()函数
#作用类似于eval()函数，但只执行，没有返回结果
x = 100
y = 10
z = exec('x+y')
print(z)