s = []
for n in range(1,1000):
	for i in range(1,n):
		if n%i==0:
			s.append(i)
	if sum(s)==n:
		print(n)
		print(s)
	s = []		