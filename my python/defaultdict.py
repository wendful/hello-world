#defaultdict:当直接读取dict不存在的属性时，直接返回默认值
from collections import defaultdict
d1 = {'one':1, 'two':2, 'three':3}
funC = lambda:'哈哈，没有哟'
d2 = defaultdict(funC)
d2['one']=1
print(d2['one'])
print(d2['four'])
