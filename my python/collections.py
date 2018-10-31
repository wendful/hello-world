#collections模块
#namedtuple；tuple类型，是一个可命名的tuple
import collections
Point = collections.namedtuple('Point', ['x','y'])
p = Point(11,22)
print(p.x)
#也可以通过下标索引
print(p[0])
#deque；比较方便的解决了频繁删除插入带来的效率问题
from collections import deque
q = deque(['a', 'b', 'c'])
print(q)
#在后面加入一个'd'
q.append('d')
print(q)
#在左边即在前面加入一个'e'
q.appendleft('e')
print(q)
