for n in range(100,1000):
	# 百位上的数字，也可以这样写：a = n //100%10
	a = (int(str(n)[0]))**3
	# 同上，十位上的数字也可写为：b = n //10%10
	b = (int(str(n)[1]))**3
	# 个位上的数字可写为：c = n%10
	c = (int(str(n)[2]))**3
	if a+b+c==n:
		print(n)