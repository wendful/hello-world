#日历模块
#isleap；判断一年是否闰年
import calendar
#判断2018年是否是闰年，返回值是布尔值
l = calendar.isleap(2018)
print(l)
#所以，获取用户输入，并判断是否是闰年的代码可以如下
#year = int(input('请输入年份:'))
#l = calendar.isleap(year)
#print(l)