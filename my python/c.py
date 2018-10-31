hour, minute, second = input('请输入时间（h:m:s):\n').split(':')

hour = int(hour)

minute = int(minute)

second = int(second)

second = second + 30

if second >= 60:

	second = second -60

	minute = minute + 1

minute = minute + 5

if minute >= 60:

	minute = minute -60

	hour = hour + 1

if hour == 24:

	hour = 0

print(f'{hour}:{minute}:{second}')	

#print('%d:%d:%d' %(hour,minute,second))

# 以上两种都可行，都是字符串的格式化