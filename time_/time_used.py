import time

ticks = time.time()
print("当前时间戳为：", ticks)

localtime = time.localtime(time.time())
print("本地时间为：", localtime)

# 格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：", localtime)

# 格式化成 2016-03-12 11:45:34
print(time.strftime("%Y-%m-%d %H:%M:%S:%s", time.localtime()))

# 格式化成 Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y"))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

"""

# 获取某月日历
import calendar

Nov = calendar.month(2017, 11)
print("输出2017年11月份的日历：")
print(Nov)

print("----------------")

print("time.altzone %d" % time.altzone)

t = time.localtime()
print("time.asctime(t) : %s" % time.asctime(t))

print(time.clock())

print("=================")
print(time.ctime())
print(time.localtime(2))
print(time.asctime())