#python语言的高级特性
#函数式编程
#lambda表达式（匿名函数）
#以lambda开头，后面跟一定的参数（如果有的话）
#参数后用冒号和表达式主体隔开
#案例1，计算一个数字的100倍
stm = lambda x : 100*x
#直接调用
print(stm(90))
#案例2，多个参数
stm2 = lambda x, y, z : x+y*10+z*100
print(stm2(2,3,4))