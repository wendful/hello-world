#datetime.datetime:提供日期跟时间的组合
#fromtimestamp:从时间戳中返回本地时间
import time
from datetime import datetime
dt = datetime(2018,10,23)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))