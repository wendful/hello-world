num = []

for n in range(1,100):
	if n%3==0 or n%7==0:
		num.append(n)
		if n%3==0 and n%7==0:
			num.remove(n)
print(len(num))		
	
	
