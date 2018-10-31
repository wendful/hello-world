sum = 0
n = 1
for n in range(1,1000):
	if n%3==0 and n%5==0 and n%7==0:
		sum += n
	n=n+1
print(sum)