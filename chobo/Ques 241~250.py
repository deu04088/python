# 241번
import datetime

d = datetime.datetime.now()
print(d)

# 242번
print(d, type(d))

# 243번
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = d - delta
    print(date)

# 244번
d = datetime.datetime.now()
print(d.strftime("%H:%M:%S"))

# 245번
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

# 246번
import time

while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

# 247번

# 248번
import os
ret = os.getcwd()
print(ret, type(ret))

# 249번
import os
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250번
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)
