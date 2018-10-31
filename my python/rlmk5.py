#日历模块
#monthrange():获取某月从周几开始和这个月的天数
#周一到周日用0~6表示
import calendar
s = calendar.monthrange(2018,9)
print(s)