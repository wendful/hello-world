#跟日历相关的模块
#calendar
import calendar
#生成2018年的日历
#w:每个日期之间的间隔字符数
#l；没周所占的行数
#c；每个月之间的间隔字符数
cal = calendar.calendar(2018,l=0,c=5,w=1)
print(cal)