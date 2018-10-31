n = int(input("请输入一个大于1的数字:"))

for i in range(2,n):
	if n%i == 0:
		print("不是质数")
		break
else:
	print("是质数")
	