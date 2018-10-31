year, month, day = input("请输入年月日（y-m-d)\n").split("-") 

year = int(year)

month = int(month)

day = int(day)

sum = day

days = [31,28,31,30,31,30,31,31,30,31,30,31]

i = 0

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
	days[1] = 29

while i< month-1:
	sum=sum+days[i]
	i=i+1
print("第",sum,"天")	