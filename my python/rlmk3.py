#日历模块
#leapdays；获取指定年份之间的闰年个数
import calendar
#获取1983年到2085年之间一共有多少个闰年
l = calendar.leapdays(1983,2085)
print(l)